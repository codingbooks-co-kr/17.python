fruits = ["apple", "banana", "cherry", "blueberry"]

# ❶ 길이가 6 이상인 단어 요소만 추출
for fruit in fruits:        	# fruits의 각 문자열을 순회
    if len(fruit) >= 6: 	# 만약 단어의 길이가 6 이상이면
        print(fruit) 		# 해당 단어를 출력

# ❷ 'b'를 포함하는 단어 요소만 추출
for fruit in fruits:        	# fruits의 각 문자열을 순회
    if 'b' in fruit:         	# 단어 안에 'b'가 포함되어 있으면
        print(fruit) 		# 해당 단어를 출력