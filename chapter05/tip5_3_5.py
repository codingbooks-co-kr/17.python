# (함수유형4) 누적합 계산

def get_total(start, end):
    total = 0
    for num in range(start, end+1):
        total += num
    return total		 # 반환값

total1 = get_total(1, 100)	 # 입·출력 변화
total2 = get_total(1, 500)	 # 입·출력 변화
print(total1, total2)		 # 반환값 다름
print(f"누적합: {total1+total2}")	 # 반환값 활용