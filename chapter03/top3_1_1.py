# 세 입력 정수 중 큰 수 구하기

x1 = int(input("정수1: "))
x2 = int(input("정수2: "))
x3 = int(input("정수3: "))

maximum = x1	# x1을 최댓값으로 설정
if x2 > maximum:	# x2가 더 크면 최댓값 갱신
    maximum = x2
if x3 > maximum:	# x3가 더 크면 최댓값 갱신
    maximum = x3

print(f"제일 큰 수: {maximum}")