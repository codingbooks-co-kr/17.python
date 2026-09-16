# 다섯 가지 이터러블 객체의 가변성 예시

my_list = [1, 2, 2, 3, 4]	# ❶ 리스트 (가변객체)
my_list[0] = 10		# 값 변경 가능
my_list.append(5) 		# 값 추가 가능
print(my_list)

my_dict = {'a': 1, 'b': 2}	# ❷ 딕셔너리 (가변객체)
my_dict['a'] = 10  		# 값 변경 가능
my_dict['c'] = 3    		# 항목 추가 가능
print(my_dict)

my_set = {1, 2, 3}		# ❸ 세트 (가변객체)
my_set.remove(1) 		# 요소 삭제 가능
my_set.add(4)    		# 요소 추가 가능
print(my_set)

my_str = "Python"		# ❹ 문자열 (불변객체)
# my_str[0] = "D"		# 값 변경 시 오류!

my_tuple = (1, 2, 3)	# ❺ 튜플 (불변객체)
# my_tuple[0] = 4		# 값 변경 시 오류!