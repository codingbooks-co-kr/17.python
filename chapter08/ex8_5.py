# ❶ 리스트 요소를 키로 사용, 값은 기본값(None) 설정
my_list = ['name', 'age']
result = dict.fromkeys(my_list)
print(result)

# ❷ 튜플 요소를 키로 사용, 값은 0 설정
my_tuple = ('math', 'english', 'science')
result = dict.fromkeys(my_tuple, 0)
print(result)

# ❸ 문자열 요소를 키로 사용, 값은 True 설정
my_str = "abc"
result = dict.fromkeys(my_str, True)
print(result)