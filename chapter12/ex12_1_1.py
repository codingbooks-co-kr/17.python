# ❶ 전공별 학생명 및 전공명 출력 (상속 미사용)

class ComputerStudent:	# 컴퓨터 전공생 
    def __init__(self, name, major):
        self.name = name	
        self.major = major
    def print_info(self):
        print(f"학생명: {self.name}, 전공명: {self.major}")

class MusicStudent:		# 음악 전공생
    def __init__(self, name, major):
        self.name = name	
        self.major = major
    def print_info(self):
        print(f"학생명: {self.name}, 전공명: {self.major}")

class DesignStudent:  	# 디자인 전공생
    def __init__(self, name, major):
        self.name = name	
        self.major = major
    def print_info(self):
        print(f"학생명: {self.name}, 전공명: {self.major}")

# 컴퓨터 전공 학생의 객체 생성 및 정보 출력
cs = ComputerStudent("민수", "컴퓨터")
cs.print_info()

# 음악 전공 학생의 객체 생성 및 정보 출력
ms = MusicStudent("지수", "음악")
ms.print_info()

# 디자인 전공 학생의 객체 생성 및 정보 출력
ds = DesignStudent("진우", "디자인")
ds.print_info()