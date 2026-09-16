class Student:			# 부모 클래스
    def __init__(self, name):
        self.name = name		# 공통 속성

class MusicStudent(Student):
    def __init__(self, name):
        super().__init__(name)		# 생성자 상속
        print(f"26학번: {self.name}")	# 추가 작업

ms = MusicStudent("지수")