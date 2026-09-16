# ❶ 평균 점수 계산 (함수 기반 코딩 방식) 

def get_average(kor, eng):
    return (kor + eng) / 2

# 1. 이름/국어/영어 점수 설정
name = "민수"
kor = 90
eng = 85

# 2. 함수 호출로 평균 점수 계산
average = get_average(kor, eng)

# 3. 결과 출력
print(f"학생 이름: {name}")
print(f"국어: {kor}점")
print(f"영어: {eng}점")
print(f">> 평균 점수: {average:.1f}점")