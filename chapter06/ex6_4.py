# 비밀번호에 '*'가 포함될 때까지 반복 처리

password = ""		# 빈 문자열로 초기화
while "*" not in password:
    password = input("비밀번호: ")
    if "*" not in password:
        print("경고: 비밀번호에 '*' 포함할 것!\n")

print("비밀번호가 유효합니다.")