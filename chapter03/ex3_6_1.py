# ❶ 세 입력 정수의 비교 (논리 및 비교 연산자 사용)

a = int(input("정수1: "))
b = int(input("정수2: "))
c = int(input("정수3: "))

if a == b and b == c:
    print("세 입력값은 모두 같다")
elif a == b or b == c or c == a:
    print("두 입력값은 같다")
else:
    print("세 입력값은 모두 다르다")