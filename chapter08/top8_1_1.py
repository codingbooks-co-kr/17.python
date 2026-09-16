# ❶ 1부터 5까지의 숫자별로 "짝수" 또는 "홀수"로 분류 후 새 딕셔너리 생성
result = {num: "짝수" if num % 2 == 0 else "홀수" for num in range(1, 6)}
print(result)

# ❷ 기존 딕셔너리에서 과일 수량에 따라 "있음" 또는 "없음"으로 분류 후 새 딕셔너리 생성
fruits = {"apple": 2, "banana": 0, "kiwi": 3, "blueberry": 12}
result = {fruit: "있음" if count > 0 else "없음" for fruit, count in fruits.items()}
print(result)