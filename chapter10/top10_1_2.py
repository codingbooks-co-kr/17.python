# ❷ 오류별로 나누어 처리하는 '구체적 예외 처리'

def get_division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("0으로 나누기 불가")
    return num1 / num2

try:
    a = int(input("분자 입력: "))
    b = int(input("분모 입력: "))
    result = get_division(a, b)	
except ValueError as e:
    # 문자 입력 시 숫자로 바꾸지 못해 오류
    print(f"입력 오류: {e}")
except ZeroDivisionError as e:
    # 분모에 0을 입력 시의 오류
    print(f"나눗셈 오류: {e}")
except Exception as e:
    # 위 두 오류 이외의 다른 모든 오류 발생 시
    print(f"예상치 못한 오류: {e}")
else:
    print("나눗셈 결과:", result)