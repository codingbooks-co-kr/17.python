# 학생과 점수는 포함(has-a) 관계: Student has a Grade

class Grade:		# 데이터와 성적 연산만 전담하는 독립 클래스
    def __init__(self, math, english, coding):
        self.math = math
        self.english = english
        self.coding = coding
    def get_average(self):
        return (self.math + self.english + self.coding) / 3

class Student:		# 부모 상속 없이, Grade 객체를 내부에 포함시킴
    def __init__(self, name, age, math, english, coding):
        self.name = name
        self.age = age
        self.grade = Grade(math, english, coding)	# Grade 객체를 생성한 후 저장
    def print_info(self):	# 내부에 포함된 Grade 객체의 속성에 접근하여 성적 정보 출력
        print(f"이름: {self.name}, 나이: {self.age}", end=" | ")
        print(f"수학: {self.grade.math}점 | 영어: {self.grade.english}점 | 코딩: {self.grade.coding}점")
    def print_average(self):
        print(f">> 평균 점수: {self.grade.get_average():.1f}점")

student = Student("민수", 20, 85, 97, 78)
student.print_info()
student.print_average()