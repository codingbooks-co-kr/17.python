class Student:			# 부모 클래스
    def __init__(self, name):
        self.name = name		# 공통 속성
        self.status = "재학생" 		# 공통 속성의 기본값 설정

class MusicStudent(Student):		# 자식 클래스
    def __init__(self, name):
        super().__init__(name)		# 생성자 상속
        self.status = "졸업생"		# 속성값 변경

ms = MusicStudent("지수")
print(f"{ms.name} 학생의 현 상태: {ms.status}")