# "딕셔너리" → "객체 딕셔너리"(→빠른 검색) 변환 (학생 정보 검색/수정)

class Student:			# 학생 정보를 담은 클래스
    def __init__(self, name, score):	# 생성자
        self.name = name		# 속성
        self.score = score		# 속성
    def print_info(self):		# 메서드
        print(f"이름: {self.name}, 점수: {self.score}점")

# 1. 원본 데이터 (이름과 점수 항목으로 이루어진 딕셔너리 준비)
raw_data = {"민수": 90, "지수": 85, "진우": 95}

# 2. 빈 딕셔너리 생성
students = {}

# 3. "이름: 객체" 항목을 students 딕셔너리에 추가
for name, score in raw_data.items():
    students[name] = Student(name, score)

print("\n--- [학생별 성적] ---")
for student in students.values():
    student.print_info()

print("\n--- [이름검색, 점수변경] ---")
target = "진우"			# 검색할 이름(target)
students[target].score = 100		# 진우 객체의 점수 변경 
students[target].print_info()		# 진우 객체의 정보 출력