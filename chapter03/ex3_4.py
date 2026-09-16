# 체중과 신장 입력 후 표준체중 여부 출력

weight = float(input("체중(kg): "))	# 체중 입력 (문자열→실수로 변환)
height = float(input("신장(cm): "))	# 신장 입력 (문자열→실수로 변환)

standard_weight = (height - 100) * 0.9
print(f"표준체중: {standard_weight:.1f}kg")

if weight < standard_weight * 0.9:	# 표준체중의 90% 미만인 경우
    print("현재 저체중입니다")
elif weight > standard_weight * 1.1:  	# 표준체중의 110% 초과한 경우
    print("현재 과체중입니다")
else:				# 표준체중의 90%∼110%
    print("현재 정상체중입니다")