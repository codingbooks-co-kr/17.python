# 전역변수/지역변수/속성/클래스변수를 함께 사용한 예시

school = "한국1대학"			# 전역변수(school)

class Student:
    major = "전자공학"		# 클래스변수(major)
    count = 0			# 클래스변수(count)
    def __init__(self, name, age):	# 지역변수 (→매개변수도 포함: name, age)
        self.name = name		# 속성/인스턴스변수 (self.name)
        self.age = age		# 속성/인스턴스변수 (self.age)
        Student.count += 1		# 클래스변수 값 증가
        print(f"{Student.major} 전공의 학생 수: {Student.count}")
    def print_info(self):	
        info = f"{self.name}의 대학교: {school}, 전공: {Student.major}, 나이: {self.age}"
        print(info)			# 지역변수(info)

s1 = Student("민수", 20)		# 객체(인스턴스) s1 생성
s2 = Student("진우", 24)		# 객체(인스턴스) s2 생성

print("\n[변경 전]")
s1.print_info()			# 메서드 호출
s2.print_info()			# 메서드 호출

school = "한국2대학"			# 전역변수 값 변경
Student.major = "컴퓨터공학"		# 클래스변수 값 변경 (s1, s2가 공유하는 값이 바뀜)
s1.age = 22			# 속성값 변경 (s1 객체의 독립적인 속성값만 변경)

print("\n[변경 후]")
s1.print_info()			# 메서드 호출
s2.print_info()			# 메서드 호출