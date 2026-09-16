# ❶ 문자열(불변 객체)의 += 연산 전후 주소 비교
words = "Hello"
print(words, id(words))
words += "Python"		# 문자열 덧셈 (복합할당연산)
print(words, id(words))

# ❷ 리스트(가변 객체)의 += 연산 전후 주소 비교
my_list = [1, 2]
print(my_list, id(my_list))
my_list += [3, 4]		# 리스트 덧셈 (복합할당연산)
print(my_list, id(my_list))