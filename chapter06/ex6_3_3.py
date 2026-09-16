# ❸ if문으로 입력 문자열에서 필수 문자 포함 여부 확인

email = "abc.naver.com"	# 이메일 주소

if "@" in email and "." in email:
    print("올바른 이메일 형식!")
else:
    print("잘못된 이메일 형식 (@와 .이 필요)")