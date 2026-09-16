# ❷ 삼각형 넓이 계산 (함수유형4)

def get_triangle_area(base, height):
    area = (base * height) / 2
    return area

print(f"삼각형의 넓이: {get_triangle_area(10, 7):.1f}")
print(f"삼각형의 넓이: {get_triangle_area(5.4, 20.5):.1f}")