# "중첩 딕셔너리" → "객체 딕셔너리" 변환 (학생 정보 관리)

class Student:			# 학생 정보를 담은 클래스
    def __init__(self, name, grade, score):	# 생성자
        self.name = name		# 속성
        self.grade = grade		# 속성
        self.score = score		# 속성
    def print_info(self):		# 메서드
        print(f"이름: {self.name}, 학년: {self.grade}학년, 점수: {self.score}점")

raw_data = {	# 1. 원본 데이터: 딕셔너리 안에 딕셔너리 중첩
    "민수": {"grade": 2, "score": 90},
    "지수": {"grade": 1, "score": 85},
    "진우": {"grade": 3, "score": 95}
}

students = {}	# 2. 빈 딕셔너리 생성

# 3. 딕셔너리의 항목(이름, 정보)을 꺼내 객체를 만들고 리스트에 추가
for name, info in raw_data.items():
    students[name] = Student(name, info["grade"], info["score"])

for student in students.values():	# [꿀팁11.1] 참조
    student.print_info()		# 학생 객체별 메서드 호출