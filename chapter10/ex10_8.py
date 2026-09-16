# 다중 예외 처리 및 함수를 사용하여 예외를 발생(raise)시키고 처리

def get_division(num1, num2):
    if num2 == 0:	     	  # 분모가 0일 때 직접 예외 발생
        raise ZeroDivisionError("0으로 나누기 불가!")
    return num1 / num2

try:
    a = int(input("분자 입력: "))  # 문자 입력 시 오류
    b = int(input("분모 입력: "))  # 문자 입력 시 오류
    result = get_division(a, b)	  # 분모가 0일 때 오류
except ValueError as e:	  # 입력값 예외 처리
    print(f"입력 오류: {e}")
except ZeroDivisionError as e:  # 함수에서 발생한 예외 처리
    print(f"나눗셈 오류: {e}")
else:
    print("나눗셈 결과:", result)