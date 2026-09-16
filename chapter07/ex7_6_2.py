scores = [75, 55, 92, 45]

# ❸ 60점 이상이면 "합격" 나머지는 "불합격" 판별
for score in scores:  		# 점수 리스트의 각 점수를 순회
    if score >= 60:        	# 점수가 60점 이상이면
        print(f"{score}점: 합격")
    else:              	# 점수가 60점 미만이면
        print(f"{score}점: 불합격")

# ❹ 80점 이상은 "우수", 60∼79는 "보통", 60 미만은 "미흡" 판별
for score in scores: 	# 점수 리스트의 각 점수를 순회
    if score >= 80:       	# 80점 이상
        print(f"{score}점: 우수")
    elif score >= 60:     	# 60점∼79점 
        print(f"{score}점: 보통")
    else:                	# 60점 미만
        print(f"{score}점: 미흡")