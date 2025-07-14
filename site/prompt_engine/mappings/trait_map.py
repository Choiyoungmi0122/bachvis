import json
import os

# JSON 파일 경로
json_path = os.path.join(os.path.dirname(__file__), "trait_map.json")

# trait_map.json 읽기
with open(json_path, "r", encoding="utf-8") as f:
    TRAIT_MAP = json.load(f)

def get_temperament(diagnosis):
    """주소증 이름으로 성격 매핑 가져오기"""
    return TRAIT_MAP.get(diagnosis, {
        "자극 추구": "보통",
        "위험 회피": "보통",
        "사회적 민감성": "보통"
    })

def get_temperament_label(temperament):
    """성격을 한국어 라벨로 문자열화"""
    return f"자극 추구({temperament['자극 추구']}) · 위험 회피({temperament['위험 회피']}) · 사회적 민감성({temperament['사회적 민감성']})"
