# ❷ 계좌 입·출금, 잔액 조회 (함수유형4 사용-추천)

# 입금 후 새로운 잔액을 반환하는 함수
def deposit(current_balance, amount):
    new_balance = current_balance + amount
    print(f"입금: {amount}원 (잔액: {new_balance}원)")
    return new_balance

# 출금 후 새로운 잔액을 반환하는 함수
def withdraw(current_balance, amount):
    if current_balance >= amount:
        new_balance = current_balance - amount
        print(f"출금: {amount}원 (잔액: {new_balance}원)")
        return new_balance
    else:
        print(f"출금: 잔액 부족 (잔액: {current_balance}원, 요청액: {amount}원)")
        return current_balance

# --- 메인 코드 실행 ---
balance = 0  		  # 잔액 (전역변수)
print(f"시작 잔액: {balance}원")
balance = deposit(balance, 5000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 4000) 
print(f"최종 잔액: {balance}원")