# ❷ 평균 점수 계산-1 (클래스 기반 코딩 방식)

class Student:			# 클래스
    def __init__(self):		# 생성자
        self.name = "민수"		# 속성
        self.kor = 90		# 속성
        self.eng = 85		# 속성
    def get_average(self):		# 메서드
        return (self.kor + self.eng) / 2

# 1. 학생 객체(student) 생성 (→속성 초기화)
student = Student()

# 2. 메서드 호출로 평균 점수 계산
average = student.get_average()

# 3. 결과 출력
print(f"학생 이름: {student.name}")
print(f"국어: {student.kor}점")
print(f"영어: {student.eng}점")
print(f">> 평균 점수: {average:.1f}점")