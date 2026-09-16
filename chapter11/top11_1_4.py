# 리스트-딕셔너리 조합: 순서가 보장되므로 정렬(sort)이 가능함
products = [
    {"name": "키보드", "price": 35000, "stock": 10},
    {"name": "마우스", "price": 25000, "stock": 50},
    {"name": "모니터", "price": 150000, "stock": 5}
]

# 가격이 낮은 순으로 정렬하기
products.sort(key=lambda x: x["price"])

print("[가격 낮은 순 상품 목록]")
for p in products:
    print(f"상품명: {p['name']} | 가격: {p['price']}원")