# "리스트-딕셔너리 조합" → "객체 리스트" 변환 (학생 정보 관리)

class Student:			# 학생 정보를 담은 클래스
    def __init__(self, name, grade, score):
        self.name = name		# 속성
        self.grade = grade		# 속성
        self.score = score		# 속성
    def print_info(self):		# 메서드 유형1
        print(f"이름: {self.name}, 학년: {self.grade}학년, 점수: {self.score}점")

raw_data = [			# 원본 데이터: 리스트 안에 딕셔너리 중첩
    {"name": "민수", "grade": 2, "score": 90},
    {"name": "지수", "grade": 1, "score": 85},
    {"name": "진우", "grade": 3, "score": 95}
]

students = []			# 빈 리스트 생성
for data in raw_data:		# raw_data에서 학생 정보 딕셔너리(data)를 하나씩 꺼내기
    student = Student(data["name"], data["grade"], data["score"])	# 객체 생성
    students.append(student)		# 생성된 객체(student)를 리스트(students)에 추가

for student in students:		# 객체 리스트에서 객체 하나씩 가져오기
    student.print_info()		# 학생 객체별 메서드 호출