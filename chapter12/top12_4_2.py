# 모든 객체는 object 클래스의 인스턴스
# [심화11.4] "파이썬에서 모든 것은 객체" 참조

print("[1. 기본 자료형]")
print("int:", type(10), isinstance(10, object))
print("float:", type(3.14), isinstance(3.14, object))
print("bool:", type(True), isinstance(True, object))
print("str:", type("Hello"), isinstance("Hello", object))
print("None:", type(None), isinstance(None, object))

print("\n[2. 컬렉션 자료형]")
print("list:", type([1, 2, 3]), isinstance([1, 2, 3], object))
print("dict:", type({"a": 1}), isinstance({"a": 1}, object))
print("tuple:", type((4, 5)), isinstance((4, 5), object))
print("set:", type({6, 7}), isinstance({6, 7}, object))

print("\n[3. 함수]")
def my_function():
    pass
print("함수:", type(my_function), isinstance(my_function, object))

print("\n[4. 사용자 정의 클래스와 인스턴스]")
# 클래스와 그 클래스로 찍어낸 인스턴스 모두 객체
class MyClass:
    pass
my_instance = MyClass()
print("클래스:", type(MyClass), isinstance(MyClass, object))
print("인스턴스:", type(my_instance), isinstance(my_instance, object))

print("\n[5. 모듈]")
import random
print("모듈:", type(random), isinstance(random, object))

print("\n[6. 예외]")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("예외 클래스:", type(ZeroDivisionError), isinstance(ZeroDivisionError, object))