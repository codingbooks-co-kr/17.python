# ❷ 여러 점수의 합계 출력 (여러 값 전달 및 반환)

def get_sum(*scores):		# 튜플 패킹1
    total = sum(scores)
    return scores, total		# 튜플 패킹2

scores, total = get_sum(75, 92, 88)	# 튜플 언패킹
print(f"{scores}의 합계: {total}")

scores, total = get_sum(85, 66, 72, 98, 55)
print(f"{scores}의 합계: {total}")