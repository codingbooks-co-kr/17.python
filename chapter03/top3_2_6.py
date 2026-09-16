# ❸ 점수에 따라 학점 평가 (명시적 범위 지정)

score = int(input("점수: "))
if score < 0 or score > 100:	# 오류 범위
    print("평가 불가!")
elif 90 <= score <= 100: 	# 90점∼100점
    print("학점: A")
elif 80 <= score < 90:  	# 80점∼89점
    print("학점: B")
elif 70 <= score < 80: 	# 70점∼79점
    print("학점: C")
elif 60 <= score < 70:	# 60점∼69점
    print("학점: D")
else: 			# 0점∼59점
    print("학점: F")