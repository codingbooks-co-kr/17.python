# 체중과 신장 입력 후 표준체중 여부 출력

weight = float(input("체중(kg): "))		# ❶ 체중 입력
height = float(input("신장(cm): "))		# ❷ 신장 입력

standard_weight = (height - 100) * 0.9		# ❸ 표준체중 계산
print(f"표준체중: {standard_weight:.1f}kg")		# ❹ 표준체중 출력

if weight < standard_weight * 0.9:	  	# ❺ 표준체중의 90% 미만
    print("저체중")
elif weight > standard_weight * 1.1:  		# ❻ 표준체중의 110% 초과
    print("과체중")
else:				  	# ❼ 이외 경우는 정상체중
    print("정상체중")