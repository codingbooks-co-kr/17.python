# 딕셔너리 함축을 사용한 리스트의 중복 요소 제거 
# 원본 리스트의 요소들이 등장한 순서 유지
my_list = [1, 1, 2, 2, 4, 3, 3]
my_dict = {x: None for x in my_list} 	# 딕셔너리 함축
result = list(my_dict)		# 리스트 변환
print(result)