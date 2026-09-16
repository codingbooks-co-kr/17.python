# ❶ (비추천) 이름을 생략한 '포괄적 예외 처리'

try:
    with open("data.txt", "r", encoding="utf-8") as file:
        for line in file:	# 파일 한 줄씩 읽기
            print(line.strip())	# 파일 내용 출력
except:
    # 모든 오류를 한 번에 잡기
    print("오류 발생!")