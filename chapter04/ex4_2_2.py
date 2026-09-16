# ❷ 점수 출력을 반복 처리

min_score = int(input("최소점수: "))
max_score = int(input("최고점수: "))
step = int(input("점수간격: "))

for score in range(min_score, max_score, step):
    print(f"점수: {score}점")