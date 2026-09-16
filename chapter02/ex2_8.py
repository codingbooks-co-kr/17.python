# 이름과 신장 입력 후 표준체중 계산

name = input("이름: ")			# 이름 입력(문자열)
height = float(input("신장(cm): "))		# 신장 입력(문자열→실수로 변환)

standard_weight = (height - 100) * 0.9		# 표준 체중 계산 
print(f"이름: {name}, 신장: {height:.1f}cm, 표준체중: {standard_weight:.1f}kg")