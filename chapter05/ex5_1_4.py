# 사용자 정의 함수 유형4 (매개변수O, 반환값O)

def greet(name):	     # 함수 정의 (매개변수O)
    message = f"안녕하세요, {name}님!"
    return message	     # 반환값O

message = greet("민수")  # 함수 호출 (인수O)
print(message)

message = greet("지수")  # 함수 호출 (인수O)
print(message)