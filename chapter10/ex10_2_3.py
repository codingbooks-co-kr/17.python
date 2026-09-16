# ❸ 이름과 점수가 리스트로 묶인 중첩 리스트 데이터
data = [ ["민수", 95], ["지수", 88], ["소라", 72] ]

with open("data.txt", "w", encoding="utf-8") as file:
    for name, score in data:
        file.write(f"{name} {score}\n")
print("중첩 리스트 데이터 쓰기 완료!")