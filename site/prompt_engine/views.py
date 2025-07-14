import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from prompt_engine.gpt_utils import call_gpt_with_profile, call_gpt_for_question
from prompt_engine.mappings.trait_map import get_temperament, get_temperament_label
import os

# 질문 목록 로딩
with open("C:/Users/Young-Mi Choi/Desktop/dev/bachvis/site/prompt_engine/mappings/questions.json", "r", encoding="utf-8") as f:
    QUESTION_LIST = json.load(f)

@csrf_exempt
def generate_virtual_patient(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            diagnosis = data.get("diagnosis")
            user_data = {
                "name": data.get("name"),
                "gender": data.get("gender"),
                "age": data.get("age"),
                "diagnosis": diagnosis
            }

            # 기질 매핑
            temperament = get_temperament(diagnosis)
            temperament_label = get_temperament_label(temperament)

            # 프롬프트 생성
            profile = call_gpt_with_profile(user_data, temperament)

            # 질문-응답 생성
            responses = []
            for q in QUESTION_LIST:
                gpt_answer = call_gpt_for_question(profile, q["question"])
                responses.append({
                    "question": q["question"],
                    "trait": temperament_label,
                    "answer": gpt_answer
                })

            return JsonResponse({
                "profile": profile,
                "trait": temperament_label,
                "responses": responses
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "POST 요청만 허용됩니다."}, status=405)
