# 평균 점수 계산-3 (클래스 기반 코딩 방식)

class Student:    		# 학생 클래스
    def __init__(self, name, kor, eng, math):	
        self.name = name   	# 속성 초기화
        self.kor = kor     	# 속성 초기화
        self.eng = eng     	# 속성 초기화
        self.math = math    # 속성 초기화
    def get_average(self):	# 메서드
        return (self.kor + self.eng + self.math) / 3

# 1. 키보드로부터 데이터 입력받기
name = input("학생 이름 입력: ")	# 문자열 입력
kor = int(input("국어 점수 입력: "))	# 숫자문자열→정수 변환
eng = int(input("영어 점수 입력: "))	# 숫자문자열→정수 변환
math = int(input("수학 점수 입력: "))	# 숫자문자열→정수 변환

# 2. 입력받은 데이터를 생성자에 전달하여 객체(student) 생성
student = Student(name, kor, eng, math)

# 3. 평균 점수 계산 (메서드 호출)
average = student.get_average()

# 4. 결과 출력
print(f"\n학생 이름: {student.name}")
print(f"국어: {student.kor}점, 영어: {student.eng}점, 수학: {student.math}점")
print(f">> 평균 점수: {average:.1f}점")