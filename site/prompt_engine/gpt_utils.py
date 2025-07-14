# gpt_utils.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_gpt_with_profile(user_data, temperament):
    prompt = f"""
당신은 자극 추구가 {temperament['자극 추구']}이고, 위험 회피는 {temperament['위험 회피']}, 사회적 민감성은 {temperament['사회적 민감성']}인 환자입니다.
이름: {user_data['name']}
성별: {user_data['gender']}
나이: {user_data['age']}
주소증: {user_data['diagnosis']}

이 환자의 심리 상태, 말투, 감정을 묘사해 주세요.
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def call_gpt_for_question(profile, question):
    """가상환자 프로필과 질문을 입력받아 GPT로 응답 생성"""
    prompt = f"""
당신은 다음과 같은 환자입니다:

{profile}

질문: {question}
환자의 응답:
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content