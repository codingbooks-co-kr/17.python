# 세트 함축을 사용한 중복 요소 제거
# 원본 리스트의 요소들이 등장한 순서 유지 안됨
my_list = ["D", "B", "B", "A", "C", "A"]
my_set = {x for x in my_list}	  # 세트 함축
result = list(my_set)		  # 리스트 변환
print(result)