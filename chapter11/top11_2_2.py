# 텍스트 파일에서 학생 정보를 읽고 객체 리스트 변환 후 출력

class Student:				# 학생 클래스
    def __init__(self, name, grade, score):	# 생성자
        self.name = name		# 속성
        self.grade = grade		# 속성
        self.score = score		# 속성
    def print_info(self):		# 메서드
        print(f"이름: {self.name}, 학년: {self.grade}학년, 점수: {self.score}점")

students = []			# 빈 리스트 생성

# 파일 열기 ('r': 읽기모드, encoding='utf-8': 한글 깨짐 방지 인코딩 설정)
with open("raw_data.txt", "r", encoding="utf-8") as file:
    for line in file:				  # 파일 내용을 한 줄씩(line) 순차적으로 읽기
        name, grade, score = line.strip().split(",")	  # 줄끝개행제거 → 쉼표분리 → 리스트언패킹
        students.append(Student(name, int(grade), int(score)))

print("--- 파일에서 읽어온 학생 명단 ---")
for student in students:	# 객체 리스트(students)에서 객체(student)를 순차적으로 가져오기
    student.print_info()	# 학생 객체(student)별 print_info() 메서드 호출