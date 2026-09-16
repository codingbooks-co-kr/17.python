# ❶ 파일 전체 읽고 출력

with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.read() 	# 파일 전체 읽기
    print(lines)