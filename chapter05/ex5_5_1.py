# ❶ 삼각형 넓이 계산 (함수유형4)

def get_triangle_area(base, height):
    area = (base * height) / 2
    return area

area1 = get_triangle_area(10, 7)
print(f"삼각형의 넓이: {area1:.1f}")

area2 = get_triangle_area(5.4, 20.5)
print(f"삼각형의 넓이: {area2:.1f}")