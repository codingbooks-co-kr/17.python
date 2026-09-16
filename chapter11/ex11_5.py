# 학생 성적 관리 프로그램 (메서드 유형1∼4 포함)

class Student:				# 학생 클래스
    def __init__(self, name):			# 생성자
        self.name = name			# 속성 초기화
        self.scores = []			# 속성 초기화 (점수를 저장할 빈 리스트 생성)
    def print_info(self):			# 메서드 유형1 (매개변수 X, 반환값 X)
        print(f"학생 이름: {self.name}")
    def add_score(self, score):		# 메서드 유형2 (매개변수 O, 반환값 X)
        self.scores.append(score)		# 리스트에 점수 추가
        print(f"{score}점 추가, 점수 리스트: {self.scores}")
    def get_average(self):			# 메서드 유형3 (매개변수 X, 반환값 O)
        return sum(self.scores) / len(self.scores)
    def check_pass(self, threshold):		# 메서드 유형4 (매개변수 O, 반환값 O)
        average = self.get_average()		# 메서드 호출
        return average >= threshold		# threshold를 넘으면 True, 아니면 False 반환

student = Student("민수")			# 객체(student) 생성
student.print_info()				# 메서드 유형1 호출 (이름 출력)
student.add_score(75)			# 메서드 유형2 호출 (점수 추가)
student.add_score(90)			# 메서드 유형2 호출 (점수 추가)
student.add_score(85)			# 메서드 유형2 호출 (점수 추가)

threshold = 80				# 합격 최소 점수
average = student.get_average()		# 메서드 유형3 호출 (평균 점수 출력)
print(f">> 평균 점수: {average:.1f}점")

if student.check_pass(threshold):		# 메서드 유형4 호출 (합격 여부 판별)
    print(">> 결과: 합격입니다.")
else:
    print(">> 결과: 불합격입니다.")