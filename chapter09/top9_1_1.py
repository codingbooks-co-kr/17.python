# ❶ iter()와 next() 사용 (수동으로 반복 제어)

my_list = [1, 2, 3]

# (1) 이터러블 객체→이터레이터 객체 변환
it = iter(my_list)

# (2) next() 함수로 값을 하나씩 가져옴
print(next(it))
print(next(it))
print(next(it))

try:
    next(it)
except StopIteration:
    print("모든 항목 순회 완료!")