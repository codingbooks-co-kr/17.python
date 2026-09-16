# ❷ 삼각형 넓이 계산 (함수유형3)

def get_triangle_area():	# 함수 정의
    base = 10		# 밑변
    height = 7		# 높이
    area = (base * height) / 2
    return area 		# 넓이값 반환

print(f"삼각형의 넓이: {get_triangle_area():.1f}")