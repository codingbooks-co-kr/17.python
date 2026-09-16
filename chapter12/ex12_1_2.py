# ❷ 전공별 학생명 및 전공명 출력 (상속 사용)

class Student:		# 부모 클래스
    def __init__(self, name, major):
        self.name = name	# 공통 속성
        self.major = major	# 공통 속성
    def print_info(self):	# 공통 메서드
        print(f"학생명: {self.name}, 전공명: {self.major}")

# Student를 상속받은 자식 클래스1
class ComputerStudent(Student):
    def __init__(self, name, major):
        super().__init__(name, major)

# Student를 상속받은 자식 클래스2
class MusicStudent(Student):
    def __init__(self, name, major):
        super().__init__(name, major)

# Student를 상속받은 자식 클래스3
class DesignStudent(Student):
    def __init__(self, name, major):
        super().__init__(name, major)

# 컴퓨터 전공 학생의 객체 생성 및 정보 출력
cs = ComputerStudent("민수", "컴퓨터")
cs.print_info()

# 음악 전공 학생의 객체 생성 및 정보 출력
ms = MusicStudent("지수", "음악")
ms.print_info()

# 디자인 전공 학생의 객체 생성 및 정보 출력
ds = DesignStudent("진우", "디자인")
ds.print_info()