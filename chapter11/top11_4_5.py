x = 10		# 숫자 객체
print(x.bit_length())

s = "python"	# 문자열 객체
print(s.upper())

l = [10, 20]	# 리스트 객체
l.append(30)	# 항목 추가
print(l)

d = {'name': '민수'}	# 딕셔너리 객체
print(d.keys())

import math	# 모듈 객체
print(math.pi)

def greet():	# 함수 객체
    print("안녕하세요")
print(greet.__name__)	

class Student:	# 클래스 객체
    def __init__(self, name):
        self.name = name
print(Student.__name__)