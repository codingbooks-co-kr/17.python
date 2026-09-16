# ❶ 두 입력 정수의 다양한 연산

x = float(input("숫자1: "))
y = float(input("숫자2: "))
sign = input("연산부호: ")

if sign == "+":		# 덧셈
    print(f"{x} {sign} {y} = {x + y}")
elif sign == "-":		# 뺄셈
    print(f"{x} {sign} {y} = {x - y}")
elif sign == "*":		# 곱셈
    print(f"{x} {sign} {y} = {x * y}")
elif sign == "/":		# 나눗셈
    print(f"{x} {sign} {y} = {x / y}")
elif sign == "//":		# 몫
    print(f"{x} {sign} {y} = {x // y}")
elif sign == "%":		# 나머지
    print(f"{x} {sign} {y} = {x % y}")
elif sign == "**":		# 거듭제곱
    print(f"{x} {sign} {y} = {x ** y}")
else:
    print("연산 오류!")