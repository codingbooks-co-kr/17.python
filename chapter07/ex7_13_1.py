# ❶ 특정 숫자 규칙 찾기: 숫자 요소 중 짝수만 포함하는 리스트 생성
result = []  			# 빈 리스트 생성
for n in range(1, 11):  		# 1∼10의 숫자를 순회
    if n % 2 == 0:      		# 만약 i가 짝수이면
        result.append(n) 		# 리스트에 i를 추가
print(result)

# ❷ 불필요한 데이터 제거: 음수를 제거한 새로운 리스트 생성
nums = [1, -2, 3, -4, 0, 6, -7, 8, 9]
result = []  			# 빈 리스트 생성
for n in nums: 			# 리스트의 숫자 요소를 순회
    if n > 0:           		# 만약 i가 0보다 크면
        result.append(n) 		# 리스트에 i를 추가
print(result)

# ❸ 특정 패턴의 문자열 찾기: '.txt' 확장자를 가진 파일명만 추출
filenames = ["a.txt", "b.png", "c.pdf", "d.txt"]
result = []  			# 빈 리스트 생성
for f in filenames: 			# 리스트의 파일명 요소를 순회
    if f.endswith('.txt'): 		# 파일명이 '.txt'로 끝나면
        result.append(f) 		# 리스트에 파일명을 추가
print(result)