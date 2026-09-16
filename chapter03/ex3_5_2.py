# ❷ 두 입력 정수의 다양한 연산 (추천 방식)

x = float(input("숫자1: "))
y = float(input("숫자2: "))
sign = input("연산부호: ")

if sign == "+":		# 덧셈
    result = x + y
elif sign == "-":		# 뺄셈
    result = x - y
elif sign == "*":		# 곱셈
    result = x * y
elif sign == "/":		# 나눗셈
    result = x / y
elif sign == "//":		# 몫
    result = x // y
elif sign == "%":		# 나머지
    result = x % y
elif sign == "**":		# 거듭제곱
    result = x ** y
else:
    result = "연산 오류!"

print(f"{x} {sign} {y} = {result}")