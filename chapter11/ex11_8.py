# "딕셔너리" → "객체 리스트"(→순서가 중요) 변환 (학생 성적순 정렬)

class Student:			# 학생 정보를 담은 클래스
    def __init__(self, name, score):	# 생성자
        self.name = name		# 속성
        self.score = score		# 속성
    def print_info(self):		# 메서드
        print(f"이름: {self.name}, 점수: {self.score}점")

# 1. 원본 데이터 (이름과 점수 항목으로 이루어진 딕셔너리 준비)
raw_data = {"민수": 90, "지수": 85, "진우": 95}

# 2. 빈 리스트 생성
students = []

# 3. 딕셔너리의 항목(이름, 점수)을 꺼내 Student 객체를 만들고 리스트에 추가 
for name, score in raw_data.items():
    students.append(Student(name, score))

print("\n--- [학생별 성적] ---")
for student in students:
    student.print_info()

# 4. 리스트 및 sort()를 사용해서 성적순(내림차순) 정렬
students.sort(key=lambda x: x.score, reverse=True)

print("\n--- [성적순 정렬] ---")
for student in students:
    student.print_info()