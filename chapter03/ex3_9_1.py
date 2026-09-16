# ❶ 사용자명과 비밀번호 일치 여부 확인
# 중첩 if문 사용

username = "admin"
password = "1234"

id = input("사용자명: ")
pw = input("비밀번호: ")

if id == username:
    if pw == password:
        print(f"안녕하세요, {username}님")
    else:
        print("비밀번호 오류!")
else:
    print("사용자명 오류!")