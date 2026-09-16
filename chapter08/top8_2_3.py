# 합집합, 교집합, 차집합, 대칭차집합, 부분집합, 상위집합

a = {1, 2, 3}
b = {2, 3, 4}
c = {2, 3}

print(a | b)	# 합집합 (두 세트의 모든 요소를 포함)
print(a.union(b))

print(a & b)	# 교집합 (두 세트의 공통 요소만 포함)
print(a.intersection(b))
print(a.isdisjoint(b))  # a와 b의 공통 요소 없으면 True

print(a - b)	# 차집합 (a 세트에만 있는 요소)
print(a.difference(b))

print(b - a)	# 차집합 (b 세트에만 있는 요소)
print(b.difference(a))

print(a ^ b)	# 대칭차집합 (a, b의 서로 다른 요소만 추출)
print(a.symmetric_difference(b))

print(a <= c)	# 부분집합 (a는 c의 부분집합이면 True)
print(a.issubset(c))

print(a >= c)	# 상위집합 (a는 c의 상위집합이면 True)
print(a.issuperset(c))