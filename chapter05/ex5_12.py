# 함수 기반 여러 점수에서 최솟값, 최댓값, 합계, 평균 계산

def get_calculation(*scores):				# 튜플 패킹1
    min_val = min(scores)				# 최솟값 구하기
    max_val = max(scores)				# 최댓값 구하기
    sum_val = sum(scores)				# 합계 구하기
    average_val = sum_val / len(scores)		# 평균 구하기
    return scores, min_val, max_val, sum_val, average_val	# 튜플 패킹2

scores, min_val, max_val, sum_val, average_val = get_calculation(75, 92, 88)	       # 튜플 언패킹
print(f"{scores}의 최솟값: {min_val}, 최댓값: {max_val}, 합계: {sum_val}, 평균: {average_val:.1f}")

scores, min_val, max_val, sum_val, average_val = get_calculation(85, 66, 72, 98, 55)  # 튜플 언패킹
print(f"{scores}의 최솟값: {min_val}, 최댓값: {max_val}, 합계: {sum_val}, 평균: {average_val:.1f}")