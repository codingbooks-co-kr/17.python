# set()을 사용한 리스트의 중복 요소 제거
# 원본 리스트의 요소들이 등장한 순서 유지 안됨
my_list = [1, 1, 2, 2, 4, 3, 3]
my_set = set(my_list)
result = list(my_set)
print(result)