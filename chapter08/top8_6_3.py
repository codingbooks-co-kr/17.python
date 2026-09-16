# for문과 if not in을 사용한 리스트의 중복 요소 제거 
# 원본 리스트의 요소들이 등장한 순서 유지
my_list = [1, 1, 2, 2, 4, 3, 3]
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)