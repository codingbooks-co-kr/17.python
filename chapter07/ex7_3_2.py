# ❷ 리스트에 입력 문자열 요소의 포함 여부 확인

words = ["한국", "일본", "미국", "러시아"]
keyword = input("키워드: ")

if keyword in words:
    print(f"리스트에 '{keyword}' 있음")
else:
    print(f"리스트에 '{keyword}' 없음")