# ❶ 문자열에서 공백을 만나면 공백없이 출력 
# continue를 활용한 공백 건너뛰기

words = "Just Do It, You Can Do It!"
for word in words:
    if word == " ": 	# 공백이면 
        continue		# 아래코드건너뛰기
    print(word, end="")