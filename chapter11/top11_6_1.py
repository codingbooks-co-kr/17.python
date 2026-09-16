# ❶ 캡슐화 미적용

class Circle:
    def __init__(self, radius):
        self.radius = radius	# 공개 속성
    def get_circumference(self):
        return 2 * 3.14 * self.radius

c = Circle(5)		# 객체 생성

print("\n[변경 전]")
print(f"반지름: {c.radius:.1f}")
print(f"원둘레: {c.get_circumference():.1f}")

# 외부에서 직접 속성을 변경할 수 있어 오류 위험!
print("\n[변경 후]")
c.radius = -5
print(f"반지름: {c.radius:.1f}")
print(f"원둘레: {c.get_circumference():.1f}")