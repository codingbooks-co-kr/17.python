# 덕 타이핑: 상속 관계가 아닌 두 클래스 모두 동일한 이름의 메서드(print_score)를 가지고 있어야 함

class ComputerStudent:		# 컴퓨터 전공 클래스 (독립적 설계)
    def __init__(self, name, theory, coding):
        self.name = name
        self.theory = theory
        self.coding = coding
    def print_score(self):  		# 메서드 이름만 맞춤
        score = self.theory * 0.4 + self.coding * 0.6
        print(f"{self.name} (컴퓨터 전공) 최종 점수: {score:.1f}점")

class MusicStudent:			# 음악 전공 클래스 (독립적 설계)
    def __init__(self, name, theory, performance):
        self.name = name
        self.theory = theory
        self.performance = performance
    def print_score(self):  		# 메서드 이름만 맞춤
        score = self.theory * 0.2 + self.performance * 0.8
        print(f"{self.name} (음악 전공) 최종 점수: {score:.1f}점")

# 상속 관계가 없는 객체들을 하나의 리스트에 담음
students = [			# 다형성 준비 (다양한 전공의 객체를 하나의 리스트에 담기)
    ComputerStudent("민수", 90, 95),
    MusicStudent("지수", 88, 92)
]

# 파이썬은 상속 관계를 묻지 않고 print_score() 메서드가 있는지만 확인
for student in students:		# 다형성 (어떤 전공인지 묻지 않고, 동일 메서드 호출)
    student.print_score()		# 다형성 (동일한 메서드 호출 → 결과는 자식별로 다름)