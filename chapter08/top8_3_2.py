# ❶ 문자열 → 리스트/튜플/세트 변환
my_str = "abc"
my_list = list(my_str)	# 문자열→리스트
print(my_list)

my_str = "Just Do It!"
my_list = my_str.split()	# 문자열→리스트
print(my_list)

my_str = "abc"
my_tuple = tuple(my_str)	# 문자열→튜플
print(my_tuple)

my_str = "aabbcc"
my_set = set(my_str)	# 문자열→세트 (중복제거, 순서없음)
print(my_set)

# ❷ 리스트/튜플/세트 (요소는 모두 문자열) → 문자열 변환
my_list = ['a', 'b', 'c']	# 리스트/튜플/세트 가능
my_str = "".join(my_list)	# 리스트→문자열
print(my_str)

my_set = {'a', 'b', 'c'}	# 리스트/튜플/세트 가능
my_str = "".join(my_set)	# 세트→문자열 (순서보장없음)
print(my_str)

my_tuple = ("kim", "lee", "park")	# 리스트/튜플/세트 가능
my_str = " : ".join(my_tuple)		# 튜플→문자열
print(my_str)

nums = (1, 2, 3)			# 리스트/튜플/세트 가능
my_str = "-".join(str(n) for n in nums)  # 튜플→문자열(제너레이터표현식)
print(my_str)			# (아래의 별도 설명 참조)

# ❸ 리스트 → 튜플 변환
my_list = [1, 2, 3]
my_tuple = tuple(my_list)		# 리스트→튜플
print(my_tuple)

# ❹ 튜플 → 리스트 변환
my_tuple = (1, 2, 3)
my_list = list(my_tuple)		# 튜플→리스트
print(my_list)

# ❺ 리스트/튜플 → 세트 변환
my_list = [1, 2, 2, 3, 1, 2]		# 리스트/튜플 가능
my_set = set(my_list)		# 리스트→세트
print(my_set)			# 세트 (중복제거, 순서없음)

# ❻ 세트 → 리스트/튜플 변환
my_set = {1, 2, 3}
my_list = list(my_set)    		# 세트→리스트 (순서보장안됨)
print(my_list)

my_set = {1, 2, 3}
my_tuple = tuple(my_set)		# 세트→튜플 (순서보장안됨)
print(my_tuple)

# ❼ 리스트/튜플/세트 → 딕셔너리 변환
# 이때, 리스트/튜플/세트는 반드시 (키,값) 쌍이어야 함
my_list = [('a', 1), ('b', 2), ('c', 3)] 	# 리스트/튜플/세트 가능
my_dict = dict(my_list)		# 리스트→딕셔너리
print(my_dict)

my_set ={('a', 1), ('b', 2), ('c', 3)} 	# 리스트/튜플/세트 가능
my_dict = dict(my_set)		# 세트→딕셔너리 (순서보장안됨)
print(my_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3}

# ❽ 딕셔너리 → 리스트/튜플/세트 변환
my_list = list(my_dict.items())
print(my_list)		# 딕셔너리(키:값)→리스트(튜플/세트 가능)

my_list = list(my_dict)
print(my_list)		# 딕셔너리(키)→리스트(튜플/세트 가능)

my_tuple = tuple(my_dict.keys())
print(my_tuple)		# 딕셔너리(키)→튜플(리스트/세트 가능)

my_set = set(my_dict.values())
print(my_set)		# 딕셔너리(값)→세트(리스트/튜플 가능)