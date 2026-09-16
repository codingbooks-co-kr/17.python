# 학생 성적 관리 프로그램 (기본값 매개변수 사용)

class Student:
    # 생성자 오버로딩 효과: kor, eng에 기본값을 0으로 설정
    def __init__(self, name, kor=0, eng=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        print(f"[{self.name}] 객체 생성 완료")
        print(f"이름: {self.name}, 국어: {self.kor}점, 영어: {self.eng}점\n")

    # 메서드 오버로딩 효과: 수정할 점수만 선택적으로 입력받도록 기본값을 None으로 설정
    def update_scores(self, kor=None, eng=None):
        if kor is not None:
            self.kor = kor
        if eng is not None:
            self.eng = eng
        print(f">> {self.name}의 성적이 업데이트됨! (국어: {self.kor}점, 영어: {self.eng}점)")

print("--- [1] 생성자 오버로딩 효과 테스트 ---")
student1 = Student("민수")		# 이름만 전달 (점수는 기본값 0으로 초기화 및 출력)
student2 = Student("지수", 75)	# 이름과 국어 점수를 전달 (영어는 기본값 0)
student3 = Student("진우", 90, 85)	# 이름과 모든 점수를 전달

print("--- [2] 메서드 오버로딩 효과 테스트 ---")
student4 = Student("민수")			# 객체 생성 시 점수 초기화
student4.update_scores(eng=85)		# 영어 점수만 업데이트 (→키워드 인수 사용)
student4.update_scores(kor=90, eng=82)	# 국어/영어 점수 업데이트 (→키워드 인수 사용)