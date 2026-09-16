# 파일을 한 줄씩 읽고 출력

try:
    with open("data.txt", "r", encoding="utf-8") as file:
        for line in file:	# 파일 한 줄씩 읽기
            print(line.strip())
except FileNotFoundError as e:
    print(f"오류: {e}")
else:
    print("\n파일 읽기 성공!")
finally:
    print("파일 처리 종료.")