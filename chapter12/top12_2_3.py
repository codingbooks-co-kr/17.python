# ❷ 부모가 요구한 메서드를 구현하지 않으면 오류!
from abc import ABC, abstractmethod

class Student(ABC):		 # 추상 클래스
    @abstractmethod
    def print_score(self):	 # 추상 메서드
        pass

class DesignStudent(Student):	 # 자식 클래스
    pass			 # 구현하지 않음!

ds = DesignStudent()	 # 오류(TypeError)