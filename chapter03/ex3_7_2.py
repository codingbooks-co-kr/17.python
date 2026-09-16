# ❷ 나이별요금구분(상향식필터링)

age = int(input("나이: "))

if age < 0:
    print("구분불가")
elif age <= 3:
    print("요금무료")
elif age <= 12:
    print("소인요금")
elif age <= 64:
    print("성인요금")
else:
    print("경로요금")