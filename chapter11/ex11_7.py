# "평행 리스트" → "객체 리스트" 변환 (학생 성적 관리)

class Student:			# 학생 정보를 담은 클래스
    def __init__(self, name, score):	# 생성자
        self.name = name		# 속성
        self.score = score		# 속성
    def print_info(self):		# 메서드
        print(f"{self.name}의 점수: {self.score}점")

# 1. 원본 데이터 (학생 이름과 점수 리스트 각각 준비)
names = ["민수", "지수", "진우"]  
scores = [90, 85, 95]

# 2. 빈 리스트 생성
students = []

# 3. zip()이 같은 위치의 이름과 점수를 짝지어 반환 → 객체생성 → 리스트에 추가
for name, score in zip(names, scores):
    student = Student(name, score)
    students.append(student)

# 4. 반복문으로 학생 객체 리스트(students)의 객체별(student) 메서드 호출
for student in students:	# 객체 리스트에서 객체 하나씩 가져오기
    student.print_info()	# 학생 객체(student)별 print_info() 메서드 호출