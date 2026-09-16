# 전공별 학생의 정보, 성적순 정렬, 통계 출력

# ==========================================
# 부모 및 자식 클래스 정의 (다형성 구조)
# ==========================================
class Student:			# 부모 클래스 (모든 공통 속성 및 메서드 정의)
    def __init__(self, name, major, theory):
        self.name = name		# 공통 속성
        self.major = major		# 공통 속성
        self.theory = theory		# 공통 속성
    def print_info(self):  		# 자식들이 오버라이딩할 기본 메서드
        print(f"학생명: {self.name}, 전공명: {self.major}, 이론: {self.theory}점", end=" | ")
    def get_score(self):		# 자식들이 오버라이딩할 기본 메서드
        pass			# '내용없음'을 뜻하는 키워드 (→[심화5.3], [꿀팁12.1] 참조)

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

# ==========================================
# 1단계: "리스트-딕셔너리 조합" → "객체 리스트" 변환
# ==========================================
raw_data = [			# 원본 데이터 (리스트-딕셔너리 조합)
    {"name": "민수", "major": "컴퓨터", "theory": 95, "practice": 90},
    {"name": "소라", "major": "컴퓨터", "theory": 68, "practice": 77},
    {"name": "지수", "major": "음악", "theory": 90, "practice": 82},
    {"name": "진우", "major": "디자인", "theory": 88, "practice": 76}
]

students = []   			# 빈 리스트 생성
for data in raw_data:		# raw_data에서 학생 정보 딕셔너리(data)를 하나씩 꺼내기
    if data["major"] == "컴퓨터":	# 컴퓨터 전공: ComputerStudent 객체생성→student 저장
        student = ComputerStudent(data["name"], data["major"], data["theory"], data["practice"])
    elif data["major"] == "음악":
        student = MusicStudent(data["name"], data["major"], data["theory"], data["practice"])
    elif data["major"] == "디자인":
        student = DesignStudent(data["name"], data["major"], data["theory"], data["practice"])
    students.append(student)		# 생성된 객체(student)를 리스트(students)에 추가

# ==========================================
# 2단계: 성적 기준 내림차순 정렬
# (students[0]: 정렬된 리스트의 첫 번째 학생으로 최고 득점자)
# ==========================================
students.sort(key=lambda student: student.get_score(), reverse=True)

# ==========================================
# 3단계: 정렬된 결과 출력 및 통계
# ==========================================
print("\n=== 학생별 최종 성적 현황 (높은 순) ===")
total_score = 0
for student in students:  		# 다형성 (전공에 상관없이 동일 메서드 호출)
    student.print_info()		# 다형성 (동일한 메서드 호출 → 결과는 자식별 다름)
    score = student.get_score() 	# 다형성 (동일한 메서드 호출 → 결과는 자식별 다름)
    print(f">> 최종 환산 점수: {score:.1f}점")
    total_score += score    		# 총점 누적

print("\n=== 통계 결과 출력 ===")
average = total_score / len(students)
print(f"전체 평균 점수: {average:.1f}점")
print(f"최고 득점자: {students[0].name} ({students[0].get_score():.1f}점)")