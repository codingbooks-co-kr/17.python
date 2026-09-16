# (오류) 키가 'a'로 시작하면 해당 항목 삭제
fruits = {"apple": 1000, "banana": 2500, "cherry": 5000}
for item in fruits.keys():		# 오류 발생!
    if item.startswith("a"):
        del fruits[item]		# 항목 삭제: [꿀팁8.4] 참조
print(fruits)