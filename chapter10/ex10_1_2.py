# ❷ 파일 쓰기 (추천)

# data.txt 파일을 쓰기모드('w')로 열어 데이터 저장
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("민수 95\n")
    file.write("지수 88\n")

print("파일 생성 및 쓰기 완료!")