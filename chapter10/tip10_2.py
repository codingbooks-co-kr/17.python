# 점수 리스트를 파일에 쓴 후 다시 읽기

# 1. 파일 쓰기
out_lines = ["민수 95\n", "지수 88\n", "진우 78\n"]		# 리스트 데이터를 파일로 저장
with open("data.txt", "w", encoding="utf-8") as file:
    file.writelines(out_lines)				# 리스트의 모든 요소를 한 번에 쓰기
print(">> 파일 쓰기 완료, 읽기 시작")

# 2. 파일 읽기
with open("data.txt", "r", encoding="utf-8") as file:	
    in_lines = file.readlines()		# 파일의 각 줄을 요소로 하는 리스트를 반환
print(in_lines)			# 읽은 리스트 확인용 출력

for line in in_lines:			# 리스트를 순회하며 출력
    print(line.strip()) 		# strip()으로 끝의 줄바꿈문자(\n) 제거