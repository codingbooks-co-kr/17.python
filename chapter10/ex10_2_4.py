# ❹ 이름과 점수 항목으로 구성된 리스트-딕셔너리 조합 데이터

data = [
    {"name": "민수", "score": 95},
    {"name": "지수", "score": 88},
    {"name": "소라", "score": 72} 
]

with open("data.txt", "w", encoding="utf-8") as file:
    for student in data:
        name = student["name"]
        score = student["score"]
        file.write(f"{name} {score}\n")
print("리스트-딕셔너리 조합 데이터 쓰기 완료!")