# 리스트의 덧셈(연결), 곱셈(반복) 연산

# [1] 문자열 리스트의 덧셈(연결) 및 곱셈(반복)
list1 = ["배", "귤"]
list2 = ["사과", "포도"]
print(list1 + list2)		# 리스트 덧셈(연결)
print(list1 * 2)		# 리스트 곱셈(반복)
print(2 * list1)		# 리스트 곱셈(반복)

# [2] 숫자 리스트의 덧셈(연결) 및 곱셈(반복)
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6, 7]
print(list1 + list2 + list3)	# 리스트 덧셈(연결)
print(list2 * 2)		# 리스트 곱셈(반복)
print(2 * list2)		# 리스트 곱셈(반복)

# [3] 리스트의 복합 할당 연산(+=, *=)
list1 += list2		# 리스트 덧셈(복합할당연산)
list1 += list3		# 리스트 덧셈(복합할당연산)
print(list1)

my_list = ["Python"]
my_list *= 3		# 리스트 곱셈(복합할당연산)
print(my_list)