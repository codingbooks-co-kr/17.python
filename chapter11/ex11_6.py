# 학생 성적 관리 프로그램-1 (복수 개의 객체 생성)

class Student:				# 클래스
    def __init__(self, name, kor, eng):		# 생성자
        self.name = name			# 속성
        self.kor = kor			# 속성
        self.eng = eng			# 속성
    def get_average(self):			# 메서드
        return (self.kor + self.eng) / 2

# 학생 객체(student1) 생성, 평균 점수 출력
student1 = Student("민수", 90, 85)		# 객체 생성
average1 = student1.get_average()		# 평균 계산
print(f"\n학생 이름: {student1.name}")
print(f"국어: {student1.kor}점")
print(f"영어: {student1.eng}점")
print(f">> 평균 점수: {average1:.1f}점")

# 학생 객체(student2) 생성, 평균 점수 출력
student2 = Student("지수", 75, 82)		# 객체 생성
average2 = student2.get_average()		# 평균 계산
print(f"\n학생 이름: {student2.name}")
print(f"국어: {student2.kor}점")
print(f"영어: {student2.eng}점")
print(f">> 평균 점수: {average2:.1f}점")