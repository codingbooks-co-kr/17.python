# (함수유형3) 누적합 계산

def get_total():
    total = 0
    for num in range(1, 101):
        total += num
    return total	     # 반환값

total1 = get_total()	     # 장점: 반환값 활용
total2 = get_total()	     # 단점: 항상 같은 결과
print(total1, total2)	     # 반환값 같음
print(f"누적합: {total1+total2}")	 # 반환값 활용