# ❺ 딕셔너리에 map() 함수를 적용한 예
products = {'apple': 1000, 'banana': 2500}

# 키:값 쌍을 추출, 각 값에 10% 할인율을 적용한 튜플 생성
result = map(lambda i: (i[0], i[1] * 0.9), products.items())
print(list(result))	# 딕셔너리로 출력: print(dict(result))

# 딕셔너리의 값만 추출 후 두 배로 변환
result = map(lambda price: price*2, products.values())
print(list(result))