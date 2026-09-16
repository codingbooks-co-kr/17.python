# ❷ 이름과 점수 쌍으로 구성된 딕셔너리 데이터
data = {"민수": 95, "지수": 88, "소라": 72}

with open("data.txt", "w", encoding="utf-8") as file:
    for name, score in data.items():
        file.write(f"{name} {score}\n")
print("딕셔너리 데이터 쓰기 완료!")