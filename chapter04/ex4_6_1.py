# ❶ 'q'를 입력할 때까지 문자열 반복 출력 (조건 반복)

user_input = ""		# 사용자 입력을 저장할 변수 초기화
while user_input != "q":	# 사용자 입력이 'q'가 아닌 동안 반복
    user_input = input("입력('q'는 종료): ")	# 사용자 입력
    if user_input != "q":	# 입력값이 'q'가 아닌 경우
        print("안녕, 파이썬!")

print("프로그램 종료")