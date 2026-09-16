# 쇼핑 항목을 동적으로 리스트에 추가, 삭제, 종료

items = ["바나나", "휴지", "시리얼"]
while True:
    print(f"\n쇼핑 리스트: {items}")
    print("1.추가, 2.삭제, 3.종료")
    choice = input("선택: ")
    if choice == '1':
        item = input("추가할 항목: ")
        items.append(item)
    elif choice == '2':
        del_item = input("삭제할 항목: ")
        if del_item in items:
            items.remove(del_item)
        else:
            print("해당 항목 없음!")
    elif choice == '3':
        break
    else:
        print("1, 2 3 중 하나를 입력해 주세요.")
print("종료합니다")