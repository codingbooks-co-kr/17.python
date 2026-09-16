list_a = [1, 2, 3]	# ① 리스트
list_b = list_a	# 두 변수는 동일한 객체를 참조
print(list_a, list_b)

list_a = []		# 변수는 새로운 빈 리스트 참조
print(list_a, list_b)	# list_b에는 영향을 끼치지 않음!

dict_a = {'x': 10, 'y': 20}	# ② 딕셔너리
dict_b = dict_a	# 두 변수는 동일한 객체를 참조
print(dict_a, dict_b)

dict_a = {}	# 변수는 새로운 빈 딕셔너리 참조
print(dict_a, dict_b)	# list_b에는 영향을 끼치지 않음!