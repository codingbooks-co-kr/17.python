# ❶ 과일별 총수익 계산하기
products = ["수박", "복숭아", "참외"]	# 과일 리스트
sales = [50, 100, 200]		# 판매 수량 리스트
prices = [15000, 2000, 1500] 	# 제품 단가 리스트

# zip으로 수량과 단가를 짝지어 곱해 매출액 계산 → 매출액 리스트
total_sales = [s * p for s, p in zip(sales, prices)]

for name, total in zip(products, total_sales):
    print(f"{name}의 총매출액: {total:,}원")