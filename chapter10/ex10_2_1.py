# ❶ 이름과 점수 요소로 구성된 리스트 데이터
data = ["민수 95", "지수 88", "소라 72"]

with open("data.txt", "w", encoding="utf-8") as file:
    for line in data:
        file.write(f"{line}\n")
print("리스트 데이터 쓰기 완료!")