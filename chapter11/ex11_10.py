# "중첩 리스트" → "객체 리스트" 변환 (학생 정보 관리)

class Student:			# 학생 정보를 담은 클래스
    def __init__(self, name, grade, score):	# 생성자
        self.name = name		# 속성
        self.grade = grade		# 속성
        self.score = score		# 속성
    def print_info(self):		# 메서드
        print(f"이름: {self.name}, 학년: {self.grade}학년, 점수: {self.score}점")

raw_data = [		# 원본데이터: 리스트 안에 리스트 중첩
    ["민수", 2, 90],		# 이름, 학년, 점수
    ["지수", 1, 85],
    ["진우", 3, 95]
]

students = []		# 빈 리스트 생성

# 리스트 언패킹 후 객체(Student)를 생성하고 리스트(students)에 추가
for name, grade, score in raw_data:
    students.append(Student(name, grade, score))

for student in students:	# 객체 리스트에서 객체 하나씩 가져오기
    student.print_info()	# 학생 객체별 메서드 호출