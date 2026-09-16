# ❶ 사용자 정의 함수 기반 큰 수 출력

def max_num(x, y):
    if x > y:
        return x
    else:
        return y

# 함수 호출 및 결과 출력-1
result = max_num(10, 20)
print(f"큰 수: {result}")

# 함수 호출 및 결과 출력-2 (변수없이 결과 출력)
print(f"큰 수: {max_num(10, 20)}")