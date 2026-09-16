# 문자열 리스트에서 학생 정보를 읽고 파일 저장 및 객체 리스트 변환 후 출력

class Student:			# 학생 클래스
    def __init__(self, name, grade, score):	# 생성자
        self.name = name		# 속성
        self.grade = grade		# 속성
        self.score = score		# 속성
    def print_info(self):		# 메서드
        print(f"이름: {self.name}, 학년: {self.grade}학년, 점수: {self.score}점")

raw_data = [			# 원본 문자열 리스트
    "민수, 2, 90",			# 순서: 이름, 학년, 점수
    "지수, 1, 85",
    "진우, 3, 95"
]

# 파일 열기 ('w': 쓰기모드, encoding='utf-8': 한글 깨짐 방지 인코딩 설정)
with open("raw_data.txt", "w", encoding="utf-8") as file:
    for data in raw_data:		# 원본 리스트(raw_data)의 문자열을 한 줄씩(data) 꺼내기
        file.write(data + "\n")		# 문장 끝에 줄바꿈 문자("\n") 붙이기
print("raw_data.txt 파일 저장 완료")

students = []			# 빈 리스트 생성
for data in raw_data:		# 원본 리스트(raw_data)의 문자열을 한 줄씩(data) 꺼내기
    name, grade, score = data.split(",")	# 문자열을 쉼표 기준 변수 세 개에 나눠(언패킹) 담기
    student = Student(name, int(grade), int(score))
    students.append(student)	 	# 생성된 객체(student)를 리스트(students)에 추가

for student in students:	 	# 객체 리스트의 객체 꺼내기
    student.print_info()	 	# 학생 객체별 메서드 호출