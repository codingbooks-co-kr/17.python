def total_sum(a, b, c, d):
    return a + b + c + d

data1 = [10, 20]		# 리스트
data2 = (30, 40)		# 튜플

# 두 묶음을 풀어서 함수의 매개변수(4개)로 전달
result = total_sum(*data1, *data2)
print(result)