# 키보드 입력을 통해 3x3 중첩 리스트(2차원 행렬) 동적 생성하기

matrix = []		# 준비 단계
row = 3			# 생성할 행(층)의 개수
col = 3			# 생성할 열(호)의 개수
print(f">> {row}x{col} 행렬 데이터 입력 시작")

# 1단계 [행 순회]
for r in range(row):	
    row_list = []
    print(f"[{r + 1}번째 행의 데이터 {col}개 입력]")

    # 2단계 [열 순회 및 입력]
    for c in range(col):
        item = int(input(f"[{r}][{c}] 위치에 넣을 정수: "))
        row_list.append(item)

    # 3단계 [행 누적]
    matrix.append(row_list)
    print(f">> {r + 1}번째 행 완성: {row_list}\n")

print(">> 최종 중첩 리스트 확인")
print("matrix = ", matrix)