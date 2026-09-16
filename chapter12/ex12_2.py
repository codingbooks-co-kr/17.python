# 전공별 학생의 이름/전공/이론점수/실습점수/최종환산점수 출력-1

class Student:  			# 부모 클래스 (모든 공통 속성 및 메서드 정의)
    def __init__(self, name, major, theory, practice):
        self.name = name		# 자식들이 상속할 공통 속성
        self.major = major		# 자식들이 상속할 공통 속성
        self.theory = theory		# 자식들이 상속할 공통 속성
        self.practice = practice	# 자식들이 상속할 공통 속성
    def print_info(self):		# 자식들이 상속할 공통 메서드
        print(f"학생명: {self.name}, 전공명: {self.major}, 이론: {self.theory}점 | 실습: {self.practice}점")

class ComputerStudent(Student): 	# 자식 클래스1 (컴퓨터 전공 학생 클래스)
    def print_com_score(self):		# 컴퓨터 전공의 성적 계산 (이론: 40%, 실습: 60%)
        com_score = (self.theory * 0.4) + (self.practice * 0.6)
        print(f">> 최종 환산 점수: {com_score:.1f}점")

class MusicStudent(Student): 		# 자식 클래스2 (음악 전공 학생 클래스)
    def print_music_score(self):	# 음악 전공의 성적 계산 (이론: 20%, 실습: 80%)
        music_score = (self.theory * 0.2) + (self.practice * 0.8)
        print(f">> 최종 환산 점수: {music_score:.1f}점")

class DesignStudent(Student):  	# 자식 클래스3 (디자인 전공 학생 클래스)
    def print_design_score(self):	# 디자인 전공의 성적 계산 (이론: 30%, 실습: 70%)
        design_score = (self.theory * 0.3) + (self.practice * 0.7)
        print(f">> 최종 환산 점수: {design_score:.1f}점")

# 컴퓨터 전공 학생의 객체 생성 및 정보 출력 (이름, 전공, 이론점수, 실습점수)
cs = ComputerStudent("민수", "컴퓨터", 95, 90)
cs.print_info()			# 부모 클래스에서 물려받은 메서드 호출
cs.print_com_score()			# 본인 클래스(ComputerStudent)만의 메서드 호출

# 음악 전공 학생의 객체 생성 및 정보 출력 (이름, 전공, 이론점수, 실습점수)
ms = MusicStudent("지수", "음악", 90, 82)
ms.print_info()			# 부모 클래스에서 물려받은 메서드 호출
ms.print_music_score()		# 본인 클래스(MusicStudent)만의 메서드 호출

# 디자인 전공 학생의 객체 생성 및 정보 출력 (이름, 전공, 이론점수, 실습점수)
ds = DesignStudent("진우", "디자인", 88, 76)
ds.print_info()			# 부모 클래스에서 물려받은 메서드 호출
ds.print_design_score()		# 본인 클래스(DesignStudent)만의 메서드 호출