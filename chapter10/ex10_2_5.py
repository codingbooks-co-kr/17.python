# ❺ 서로 분리된 두 개의 리스트 데이터
names = ["민수", "지수", "소라"]
scores = [95, 88, 72]

with open("data.txt", "w", encoding="utf-8") as file:
    # zip 함수가 같은 인덱스의 이름과 점수를 짝지어 반환
    for name, score in zip(names, scores):
        file.write(f"{name} {score}\n")
print("zip 함수를 활용한 분리 리스트 데이터 쓰기 완료!")