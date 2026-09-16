# 1부터 입력한 정수까지의 합계 누적

total = 0
num = int(input("정수: "))
for i in range(1, num+1):
    total += i
print(f"1에서 {num}까지의 합: {total}")