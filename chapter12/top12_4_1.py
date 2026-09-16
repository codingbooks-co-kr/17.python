# 1. 부모 클래스 선언: 겉보기엔 상속이 없지만, 실제로는 class Parent(object): 와 같음
class Parent:
    pass

# 2. Parent를 상속받는 자식 클래스 선언
class Child(Parent):
    pass

# 3. 객체 생성
p = Parent()	# Parent 클래스의 인스턴스(p) 생성
c = Child()	# Child 클래스의 인스턴스(c) 생성

# [검증 1] 모든 클래스는 object 클래스의 자식 클래스(subclass)인가?
print("Parent는 object 클래스의 자식 클래스인가?:", issubclass(Parent, object))
print("Child는 object 클래스의 자식 클래스인가?:", issubclass(Child, object))

# [검증 2] 모든 객체는 object 클래스의 인스턴스(instance)인가?
print("p는 object 클래스의 인스턴스인가?:", isinstance(p, object))
print("c는 object 클래스의 인스턴스인가?:", isinstance(c, object))

# [검증 3] object가 물려준 족보(MRO) 확인하기 (__mro__는 상속 계층도(탐색 순서)를 반환하는 메서드)
print("Child 클래스의 족보 경로:", Child.__mro__)