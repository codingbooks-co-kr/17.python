list_a = [1, 2, 3]		# ① 리스트
list_b = list_a 		# 두 변수는 동일한 객체를 참조
print(list_a, list_b)

list_a.clear()		# list_a가 참조하는 객체를 비움
print(list_a, list_b)		# list_b 객체도 비워짐

dict_a = {'x': 10, 'y': 20}	# ② 딕셔너리
dict_b = dict_a 		# 두 변수는 동일한 객체를 참조
print(dict_a, dict_b)

dict_a.clear()		# dict_a가 참조하는 객체를 비움
print(dict_a, dict_b)		# dict_b 객체도 함께 비워짐