# ❸ 리스트에 입력 정수 요소의 포함 여부 확인

nums = [1, 2, 3, 4, 5]
keynum = int(input("정수: "))

if keynum not in nums:
    print(f"리스트에 '{keynum}' 없음")
else:
    print(f"리스트에 '{keynum}' 있음")