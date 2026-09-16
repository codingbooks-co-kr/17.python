# ❷ 파일을 한 줄씩 반복적으로 읽고 출력 (추천)

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file: 		# 파일 한 줄씩 읽기
        print(line.strip())