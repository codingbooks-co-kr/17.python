# 학점 계산

score = int(input("점수: "))	  # 점수 입력
if score >= 90:		  # 90점 이상
    print("학점: A")
elif score >= 80:		  # 80점 이상
    print("학점: B")
elif score >= 70:		  # 70점 이상
    print("학점: C")
elif score >= 60:		  # 60점 이상
    print("학점: D")
else:		  	  # 60점 미만
    print("학점: F")