# 쇼핑 리스트에 있는 과일을 입력받을 때까지 반복 처리

shopping_list = ["사과", "딸기", "포도", "바나나"]
shopping_item = ""		# 빈 문자열로 변수 초기화

while shopping_item not in shopping_list:
    shopping_item = input("쇼핑할 과일: ")
    if shopping_item not in shopping_list:
        print(f"'{shopping_item}': 쇼핑할 과일이 아닙니다")

print(f"'{shopping_item}': 쇼핑할 과일입니다")