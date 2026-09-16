# ❷ 'q'를 입력할 때까지 문자열 반복 출력 (무한 반복: 추천)

while True:			# 무한 반복
    user_input = input("입력('q'는 종료): ")	# 사용자 입력
    if user_input == "q":		# 사용자 입력이 'q'인 경우
        break  			# 즉시 루프 탈출
    print("안녕, 파이썬!")

print("프로그램 종료")