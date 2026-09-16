# 중첩 리스트의 예: 3x3 행렬

matrix = [	# 중첩 리스트(=2차원 행렬)의 초기화
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n--- 특정 요소에 접근 ---")
print(f"matrix[0] = {matrix[0]}")
print(f"matrix[1][2] = {matrix[1][2]}")

print("\n--- 요소 추가/수정/삭제 ---")
matrix.append([10, 11, 12])		# 행 추가
print(f"행 추가 후: {matrix}")

matrix[0][1] = 20			# 요소 수정
print(f"요소 수정 후: {matrix}")

del matrix[1]			# 행 삭제
print(f"행 삭제 후: {matrix}")

del matrix[1][1]			# 요소 삭제
print(f"요소 삭제 후: {matrix}")

print("\n--- 모든 요소 출력 ---")
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()		# 각 행이 끝날 때마다 줄바꿈