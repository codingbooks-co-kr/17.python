# 파일에 데이터를 저장한 후, 읽고 합계와 평균 계산

# 1. 파일 쓰기: [질문10.2] 참조
data = ["민수 95", "지수 88", "소라 72"]

with open("data.txt", "w", encoding="utf-8") as file:
    for line in data:
        file.write(f"{line}\n")
print("리스트 데이터 쓰기 완료!")

# 2. 파일 읽기
total = 0
count = 0
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:		# 파일 한 줄씩 읽기
        name, score = line.strip().split()
        total += int(score)	# 산술연산을 위해 문자열→정수 변환
        count += 1
        print(f"{name}의 점수: {score}")

# 3. 결과 출력
average = total / count
print(f">> 합계: {total}, 학생수: {count}, 평균: {average:.1f}")