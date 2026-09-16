# 전공별 학생의 정보(이름/전공/이론점수/실습점수/최종환산점수) 및 통계(전체평균/최고득점자) 출력

class Student:			# 부모 클래스 (모든 공통 속성 및 메서드 정의)
    def __init__(self, name, major, theory):
        self.name = name		# 공통 속성
        self.major = major		# 공통 속성
        self.theory = theory		# 공통 속성
    def print_info(self):  		# 자식들이 오버라이딩할 기본 메서드
        print(f"학생명: {self.name}, 전공명: {self.major}, 이론: {self.theory}점", end=" | ")
    def get_score(self):		# 자식들이 오버라이딩할 기본 메서드
        pass			# '내용 없음'을 뜻하는 키워드 (→[심화5.3], [꿀팁12.1] 참조)

class ComputerStudent(Student):	# 자식 클래스1 (컴퓨터 전공 학생 클래스)
    def __init__(self, name, major, theory, coding):
        super().__init__(name, major, theory)	# 부모의 생성자 호출, 공통 속성 초기화
        self.coding = coding		# 자식만의 속성 추가
    def print_info(self):      		# 메서드 오버라이딩
        super().print_info()		# 부모의 메서드 호출, 재사용
        print(f"코딩: {self.coding}점", end=" ")
    def get_score(self):		# 메서드 오버라이딩: 성적 계산 (이론: 40%, 실습: 60%)
        return (self.theory * 0.4) + (self.coding * 0.6)

class MusicStudent(Student):		# 자식 클래스2 (음악 전공 학생 클래스)
    def __init__(self, name, major, theory, performance):
        super().__init__(name, major, theory)	# 부모의 생성자 호출, 공통 속성 초기화
        self.performance = performance	# 자식만의 속성 추가
    def print_info(self):      		# 메서드 오버라이딩
        super().print_info()		# 부모의 메서드 호출, 재사용
        print(f"연주: {self.performance}점", end=" ")
    def get_score(self):		# 메서드 오버라이딩: 성적 계산 (이론: 20%, 실습: 80%)
        return (self.theory * 0.2) + (self.performance * 0.8)

class DesignStudent(Student):  	# 자식 클래스3: 디자인 전공
    def __init__(self, name, major, theory, portfolio):
        super().__init__(name, major, theory)	# 부모의 생성자 호출, 공통 속성 초기화
        self.portfolio = portfolio	# 자식만의 속성 추가
    def print_info(self):      		# 메서드 오버라이딩
        super().print_info()		# 부모의 메서드 호출, 재사용
        print(f"포트폴리오: {self.portfolio}점", end=" ")
    def get_score(self):		# 메서드 오버라이딩: 성적 계산 (이론: 30%, 실습: 70%)
        return (self.theory * 0.3) + (self.portfolio * 0.7)

students = [			# 다형성 준비 (다양한 전공의 객체를 하나의 리스트에 담기)
    ComputerStudent("민수", "컴퓨터", 95, 90),
    ComputerStudent("소라", "컴퓨터", 68, 77),
    MusicStudent("지수", "음악", 90, 82),
    DesignStudent("진우", "디자인", 88, 76)
]

print("\n=== 학생별 최종 환산 점수 현황 ===")
total_score = 0
best_student = students[0] 		# 첫 번째 학생을 기본 최고점으로 설정
for student in students:		# 다형성 (전공에 상관없이 동일 메서드 호출)
    student.print_info()		# 다형성 (동일한 메서드 호출 → 결과는 자식별 다름)
    score = student.get_score() 	# 다형성 (동일한 메서드 호출 → 결과는 자식별 다름)
    print(f">> 최종 환산 점수: {score:.1f}점")

    total_score += score 			# 총점 누적
    if score > best_student.get_score():		# 최고 득점자 찾기
        best_student = student

print("\n=== 통계 결과 출력 ===")
average = total_score / len(students)
print(f"전체 평균 점수: {average:.1f}점")
print(f"최고 득점자: {best_student.name} ({best_student.get_score():.1f}점)")