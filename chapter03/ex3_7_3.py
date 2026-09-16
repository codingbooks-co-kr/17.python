# ❸ 나이별요금구분(하향식필터링)

age = int(input("나이: "))

if age >= 65:
    print("경로요금")
elif age >= 13:
    print("성인요금")
elif age >= 4:
    print("소인요금")
elif age >= 0:
    print("요금무료")
else:
    print("구분불가")