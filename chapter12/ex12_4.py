# 전공별 학생의 이름/전공/이론점수/실습점수/최종환산점수 출력-3

class Student:			# 부모 클래스 (모든 공통 속성 및 메서드 정의)
    def __init__(self, name, major, theory):
        self.name = name		# 공통 속성
        self.major = major		# 공통 속성
        self.theory = theory		# 공통 속성
    def print_info(self):		# 자식들이 오버라이딩할 기본 메서드
        print(f"학생명: {self.name}, 전공명: {self.major}, 이론: {self.theory}점", end=" | ")
    def print_score(self):  		# 자식들이 오버라이딩할 기본 메서드
        pass			# '내용 없음'을 뜻하는 키워드 (→[심화5.3], [꿀팁12.1] 참조)

class ComputerStudent(Student):	# 자식 클래스1 (컴퓨터 전공 학생 클래스)
    def __init__(self, name, major, theory, coding):
        super().__init__(name, major, theory)		# 부모의 생성자 호출, 공통 속성 초기화
        self.coding = coding		# 자식만의 속성 추가
    def print_info(self):      		# 메서드 오버라이딩
        super().print_info()		# 부모의 메서드 호출, 재사용
        print(f"코딩: {self.coding}점", end=" ")
    def print_score(self):		# 메서드 오버라이딩: 성적 계산 (이론: 40%, 실습: 60%)
        score = (self.theory * 0.4) + (self.coding * 0.6)
        print(f">> 최종 환산 점수: {score:.1f}점")

class MusicStudent(Student):		# 자식 클래스2 (음악 전공 학생 클래스)
    def __init__(self, name, major, theory, performance):
        super().__init__(name, major, theory)		# 부모의 생성자 호출, 공통 속성 초기화
        self.performance = performance		# 자식만의 속성 추가
    def print_info(self):      		# 메서드 오버라이딩
        super().print_info()		# 부모의 메서드 호출, 재사용
        print(f"연주: {self.performance}점", end=" ")
    def print_score(self):		# 메서드 오버라이딩: 성적 계산 (이론: 20%, 실습: 80%)
        score = (self.theory * 0.2) + (self.performance * 0.8)
        print(f">> 최종 환산 점수: {score:.1f}점")

class DesignStudent(Student):  	# 자식 클래스3: 디자인 전공
    def __init__(self, name, major, theory, portfolio):
        super().__init__(name, major, theory)		# 부모의 생성자 호출, 공통 속성 초기화
        self.portfolio = portfolio	# 자식만의 속성 추가
    def print_info(self):      		# 메서드 오버라이딩
        super().print_info()		# 부모의 메서드 호출, 재사용
        print(f"포트폴리오: {self.portfolio}점", end=" ")
    def print_score(self):		# 메서드 오버라이딩: 성적 계산 (이론: 30%, 실습: 70%)
        score = (self.theory * 0.3) + (self.portfolio * 0.7)
        print(f">> 최종 환산 점수: {score:.1f}점")

# 컴퓨터 전공 학생 객체 생성 및 정보 출력 (이름, 전공, 이론, 코딩)
cs = ComputerStudent("민수", "컴퓨터", 95, 90)
cs.print_info()
cs.print_score()

# 음악 전공 학생 객체 생성 및 정보 출력 (이름, 전공, 이론, 연주)
ms = MusicStudent("지수", "음악", 90, 82)
ms.print_info()
ms.print_score()

# 디자인 전공 학생의 객체 생성 및 정보 출력 (이름, 전공, 이론, 포트폴리오)
ds = DesignStudent("진우", "디자인", 88, 76)
ds.print_info()
ds.print_score()