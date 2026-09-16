# ❷ 유효 점수 범위 확인

score = int(input("점수(0~100): "))

if not (0 <= score <= 100):
    print("잘못된 점수 범위입니다!")
else:
    print(f"정상 입력: {score}점")