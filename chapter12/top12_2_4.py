# 추상 클래스: 자식 클래스들에게 print_score() 메서드 오버라이딩 구현을 강제하는 구조

from abc import ABC, abstractmethod	# 추상 클래스 구현을 위한 모듈 불러오기

class Student(ABC):			# 추상 클래스: 모든 전공 학생의 공통 규칙
    def __init__(self, name, theory):
        self.name = name
        self.theory = theory
    @abstractmethod		# 자식 클래스가 이 메서드를 반드시 구현하도록 강제
    def print_score(self):   		# 반드시 구현해야 하는 추상 메서드
        pass

class ComputerStudent(Student):	# 자식 클래스1 (컴퓨터 전공 학생 클래스)
    def __init__(self, name, theory, coding):
        super().__init__(name, theory)
        self.coding = coding
    def print_score(self):		# 부모가 숙제로 내준 추상 메서드를 실제로 구현
        score = self.theory * 0.4 + self.coding * 0.6
        print(f"{self.name} (컴퓨터 전공) 최종 점수: {score:.1f}점")

class MusicStudent(Student):		# 자식 클래스2 (음악 전공 학생 클래스)
    def __init__(self, name, theory, performance):
        super().__init__(name, theory)
        self.performance = performance
    def print_score(self):		# 부모가 숙제로 내준 추상 메서드를 실제로 구현
        score = self.theory * 0.2 + self.performance * 0.8
        print(f"{self.name} (음악 전공) 최종 점수: {score:.1f}점")

# 상속 관계의 객체들을 하나의 리스트에 담음
students = [			# 다형성 준비 (다양한 전공의 객체를 하나의 리스트에 담기)
    ComputerStudent("민수", 90, 95),
    ComputerStudent("소라", 68, 77),
    MusicStudent("지수", 88, 92)
]

for student in students:		# 다형성 (어떤 전공인지 묻지 않고, 동일 메서드 호출)
    student.print_score()		# 다형성 (동일한 메서드 호출 → 결과는 자식별로 다름)