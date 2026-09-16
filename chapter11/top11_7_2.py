# 가변 객체 (예: 리스트)

list1 = [1, 2, 3]	# list1은 리스트 객체를 참조
print(list1, id(list1))

list1 = [4, 5, 6]	# list1은 새로운 리스트 객체를 참조
print(list1, id(list1))

list2 = list1	# list2는 list1과 동일한 객체를 참조
print(list2, id(list2))	# 같은 객체 참조하므로 ID도 같음

list1[0] = 10	# list1 객체의 요소를 변경
print(list1, id(list1))
print(list2, id(list2))	# 같은 객체를 참조하므로 list2도 변경됨