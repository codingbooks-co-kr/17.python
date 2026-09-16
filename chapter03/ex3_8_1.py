# ❶ 이름 입력의 유무 확인

name = input("이름: ")

if not name:	# 입력 없음(→엔터키만 누름)
    print("이름을 입력해 주세요!")
else:		# 입력 있음
    print(f"환영합니다, {name}님!")