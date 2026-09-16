# ❶ 이터레이터 객체 (→예: 제너레이터 표현식)
my_gen = (x for x in range(1, 4))

print("--- 첫 번째 반복 ---")
for num in my_gen:
    print(num)

print("--- 두 번째 반복 ---")
for num in my_gen:
    print(num)