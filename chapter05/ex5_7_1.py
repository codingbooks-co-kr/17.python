# ❶ 계좌 입·출금, 잔액 조회 (전역변수 사용-비추천)

balance = 0 		# 잔액 (전역변수)

def deposit(amount):	# 입금 함수
    global balance  	# 전역변수 사용선언
    balance += amount
    print(f"입금: {amount}원 (잔액: {balance}원)")

def withdraw(amount):	# 출금 함수
    global balance 		# 전역변수 사용선언
    if balance >= amount:
        balance -= amount
        print(f"출금: {amount}원 (잔액: {balance}원)")
    else:
        print(f"출금: 잔액 부족 (잔액: {balance}원, 요청액: {amount}원)")

# --- 메인 코드 실행 ---
print(f"시작 잔액: {balance}원")
deposit(5000)   	# 5000원 입금
withdraw(2000)  	# 2000원 출금
withdraw(4000)  	# 잔액 부족 상황 테스트
print(f"최종 잔액: {balance}원")