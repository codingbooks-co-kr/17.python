# ❶ 추상 클래스는 직접 객체를 만들 수 없음!
from abc import ABC, abstractmethod

class Student(ABC):	     # 추상 클래스
    @abstractmethod
    def print_score(self): # 추상 메서드
        pass

s = Student()	     # 오류(TypeError)