# ❷ 캡슐화 적용

class Circle:
    def __init__(self, radius):
        # 생성 시에도 접근자 호출→유효성 검사
        self.radius = radius

    @property		# 접근자(Getter)
    def radius(self):		# 숨겨진 값 읽기
        return self.__radius

    @radius.setter		# 설정자(Setter)
    def radius(self, value):	# 음수→0 보정
        if value < 0:
            self.__radius = 0
        else:
            self.__radius = value

    def get_circumference(self):  # 접근자 호출
        return 2 * 3.14 * self.radius

c = Circle(5)		# 설정자 호출

print("\n[변경 전]")
print(f"반지름: {c.radius:.1f}")	# 접근자 호출
print(f"원둘레: {c.get_circumference():.1f}")

# 외부에서 직접 속성을 변경 시 설정자 자동 호출
print("\n[변경 후]")
c.radius = -5		# 설정자 호출
print(f"반지름: {c.radius:.1f}")	# 접근자 호출
print(f"원둘레: {c.get_circumference():.1f}")