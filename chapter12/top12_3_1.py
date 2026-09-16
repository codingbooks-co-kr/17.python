# 학생과 사람은 상속(Is-a) 관계: Student is a Person

class Person:			# 부모 클래스 (모든 인류의 공통 속성)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):		# 자식들이 오버라이딩할 기본 메서드
        print(f"이름: {self.name}, 나이: {self.age}", end=" | ")

class Student(Person):		# 자식 클래스
    def __init__(self, name, age, math, english, coding):
        super().__init__(name, age)	# 부모의 생성자 호출, 공통 속성 초기화
        self.math = math		# 자식만의 고유 속성 추가
        self.english = english		# 자식만의 고유 속성 추가
        self.coding = coding		# 자식만의 고유 속성 추가
    def print_info(self):		# 메서드 오버라이딩
        super().print_info()  		# 부모의 메서드 호출, 재사용
        print(f"수학: {self.math}점 | 영어: {self.english}점 | 코딩: {self.coding}점")
    def get_average(self):		# 자식만의 고유 메서드
        return (self.math + self.english + self.coding) / 3

student = Student("민수", 20, 85, 97, 78)
student.print_info()
print(f">> 평균 점수: {student.get_average():.1f}점")