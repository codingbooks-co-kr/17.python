# ❷ 문자열에서 특정 문자를 만나면 종료
# break를 활용한 조기 탈출

words = "Just Do It, You Can Do It!"
for word in words:
    if word == ",":		# "," 문자이면
        break		# 루프 탈출
    print(word, end="")