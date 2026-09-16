# ❶ 모든 오류를 묶어 처리하는 '포괄적 예외 처리'

def get_division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("0으로 나누기 불가")
    return num1 / num2

try:
    a = int(input("분자 입력: "))
    b = int(input("분모 입력: "))
    result = get_division(a, b)	
except Exception as e:
    # 모든 오류에 대해 모두 이 블록에서 처리
    print(f"예상치 못한 오류: {e}")
else:
    print("나눗셈 결과:", result)