# 구구단 만들기

for x in range(1, 10):  	# 바깥쪽 루프: 1단∼9단
    print(f"[{x}단 시작]")
    for y in range(1, 10):	# 안쪽 루프: 1∼9까지 순차 곱셈
        print(f"{x} x {y} = {x * y}")
    print()            	# 한 단이 끝나면 줄바꿈
print("구구단 종료!")