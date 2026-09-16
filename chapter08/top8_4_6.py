# ❸ 여러 값을 반환 시 패킹/언패킹 (→5.6절 및 [꿀팁5.5] 참조)
def get_min_max(nums):
    return min(nums), max(nums)		# 튜플 패킹

data = [2, 1, 4, 5, 3]
minimum, maximum = get_min_max(data)	# 튜플 언패킹
print(f"최솟값: {minimum}, 최댓값: {maximum}")