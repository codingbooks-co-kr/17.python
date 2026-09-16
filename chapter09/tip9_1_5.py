# ❺ 딕셔너리에 리스트 함축을 적용한 예
products = {'apple': 1000, 'banana': 2500}

# 키:값 쌍을 추출, 각 값에 10% 할인율을 적용한 튜플 생성
result = [(k, int(v * 0.9)) for k, v in products.items()]
print(result)	# 딕셔너리로 출력: print(dict(result))

# 딕셔너리의 값만 추출 후 두 배로 변환
result = [v * 2 for v in products.values()]
print(result)