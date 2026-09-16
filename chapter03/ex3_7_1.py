# ❶ 나이별요금구분(명시적범위지정)

age = int(input("나이: "))

if 0 <= age <= 3:
    print("요금무료")
elif 3 < age <= 12:
    print("소인요금")
elif 12 < age <= 64:
    print("성인요금")
elif age > 64:
    print("경로요금")
else:
    print("구분불가")