# 3행 10열의 직사각형 별 패턴 만들기

rows = 3			# 3행
cols = 10			# 10열
for r in range(rows): 	# 바깥쪽 루프
    for c in range(cols):	# 안쪽 루프
        print("*", end=" ")
    print() 		# 줄바꿈
print("별 패턴 종료!")