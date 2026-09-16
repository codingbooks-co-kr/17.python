# ❹ 딕셔너리에 filter() 함수를 적용한 예
products = {'apple': 1000, 'banana': 2500, 'kiwi': 3000}

# 딕셔너리의 값 중 2000원 이상의 상품만 필터링
result = filter(lambda item: item[1] >= 2000, products.items())
print(dict(result))

# 딕셔너리의 키 중 'e'를 포함하는 상품만 필터링
result = filter(lambda item: 'e' in item[0], products.items())
print(dict(result))