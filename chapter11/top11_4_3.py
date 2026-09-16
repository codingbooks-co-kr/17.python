# 기본 데이터 객체 (Value Objects)

x = None		# ❶NoneType 클래스 객체
print(type(x)) 	# <class 'NoneType'>

x = 10		# ❷int 클래스의 객체
print(type(x))	# <class 'int'>

s = "python"	# ❸str 클래스의 객체
print(type(s))	# <class 'str'>

l = [1, 2, 3]	# ❹list 클래스의 객체
print(type(l))	# <class 'list'>

d = {'a':1, 'b':2}	# ❺dict 클래스의 객체
print(type(d))	# <class 'dict'>

# 구조적 객체 (Structural Objects)

def greet():	# ❻function 클래스의 객체
    print("안녕하세요")
print(type(greet))	# <class 'function'>

class Car:		# ❼type 클래스의 객체
    pass	   	# '내용없음'을 뜻하는 키워드
print(type(Car))	# <class 'type'>

import math	# ❽module 클래스의 객체
print(type(math))	# <class 'module'>