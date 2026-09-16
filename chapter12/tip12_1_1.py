# 부모 클래스: 학생의 이름만 관리하는 공통 설계도
class Student:			# 부모 클래스
    def __init__(self, name):
        self.name = name		# 부모 속성

# 자식 클래스: 부모의 이름 속성 + 자식만의 '점수' 속성 추가
class MusicStudent(Student):		# 자식 클래스
    def __init__(self, name, performance):
        super().__init__(name)		# 생성자 상속
        self.performance = performance  # 속성 추가

ms = MusicStudent("지수", 90)
print(f"{ms.name} 학생의 연주 점수: {ms.performance}점")