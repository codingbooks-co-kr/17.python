# pass, continue, break, return 사이의 차이

def check_numbers(mode):
    print(f"--- {mode} 모드 실행 ---")
    for i in range(1, 5):		# 1∼4 순차 반복
        if i == 2:			# i가 2가 되는 순간을 감지
            if mode == "pass":
                pass          	# pass: 그냥 통과! (아래의 print() 실행)
            elif mode == "break":
                break          	# break: 나를 감싸는 가장 가까운 반복문(for)만 즉시 탈출
            elif mode == "continue":
                continue      	# continue: 아래 print()를 무시, 다음 반복(i=3)으로 점프
            elif mode == "return":
                return      		# return: (반복문 포함) 함수 실행 자체를 즉시 종료
        print(f"{i}회 반복")
    print("반복문 종료!")		# [주의] return 시에는 이 줄도 실행 안 됨

# 각 모드별 실행
check_numbers("pass")
print()
check_numbers("break")
print()
check_numbers("continue")
print()
check_numbers("return")