# 여러 줄을 입력받아 리스트에 모았다가 한 번에 쓰기

print(">> 멀티 라인 메모장 (입력 종료는 빈 줄에서 Enter)")
lines = []				# 사용자가 입력한 데이터를 담을 빈 리스트 준비

# 1. 데이터를 리스트에 담기
while True:			# 무한 반복
    line = input("입력: ")		# 사용자로부터 입력받기
    if line == "":			# 빈 줄에서 Enter 키를 누르면 반복문 종료
        break
    lines.append(line)		# 입력받은 문장을 리스트에 추가

# 2. 리스트 데이터를 파일에 저장하기 (쓰기 모드 'w')
print(f">> 총 {len(lines)}줄의 데이터를 파일에 기록 시작!")
with open("data.txt", "w", encoding="utf-8") as file:
    for line in lines:		# 리스트 데이터를 한 줄씩 파일에 쓰기
        file.write(f"{line}\n")		# 문장 데이터 끝에 줄바꿈(\n) 붙이기

print(">> 파일 생성 및 쓰기 완료!")