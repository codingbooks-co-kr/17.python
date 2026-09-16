# ❷ 람다 함수와 조건부 표현식 기반 큰 수 출력

max_num = lambda x, y : x if x > y else y

# 함수 호출 및 결과 출력-1
result = max_num(10, 20)
print(f"큰 수: {result}")

# 함수 호출 및 결과 출력-2 (변수없이 결과 출력)
print(f"큰 수: {max_num(10, 20)}")