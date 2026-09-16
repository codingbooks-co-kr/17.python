# 원의 면적 계산

radius = float(input("반지름: "))		  # 입력 (반지름)

area = 3.14 * (radius ** 2)		  # 계산 (면적=π×r2)

print(f"반지름 {radius}인 원의 면적: {area}")  	 # 출력1
print(f"반지름 {radius}인 원의 면적: {area:.1f}")	 # 출력2
print(f"반지름 {radius}인 원의 면적: {round(area, 1)}") # 출력3