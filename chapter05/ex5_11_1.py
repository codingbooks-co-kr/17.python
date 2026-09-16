# ❶ 여러 점수의 합계 출력 (여러 값 전달)

def print_sum(*scores):	# 튜플 패킹
    total = sum(scores)
    print(f"{scores}의 합계: {total}")

print_sum(75, 92, 88)
print_sum(85, 66, 72, 98, 55)