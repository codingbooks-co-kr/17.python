# ❷ (추천) 원인을 콕 짚어내는 '구체적 예외 처리'

try:
    with open("data.txt", "r", encoding="utf-8") as file:
        for line in file:	# 파일 한 줄씩 읽기
            print(line.strip())	# 파일 내용 출력
except FileNotFoundError as e:
    # '파일을 찾을 수 없는 오류'만 콕 집어서 잡기
    print(f"오류: {e}")