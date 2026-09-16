# ❹ 딕셔너리에 딕셔너리 함축을 적용한 예
products = {'apple': 1000, 'banana': 2500, 'kiwi': 3000}

# 딕셔너리의 요소 중 2000원 이상의 상품만 필터링
result = {k: v for k, v in products.items() if v >= 2000}
print(result)

# 딕셔너리의 요소 중 'e'를 포함하는 상품만 필터링
result = {k: v for k, v in products.items() if 'e' in k}
print(result)