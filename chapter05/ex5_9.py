# ❶ 기본값 매개변수 예 (기본값 없는 매개변수(x)는 반드시 값을 전달해야 함)
def get_sum(x, y=0, z=0):
    return x + y + z
print(get_sum(10))
print(get_sum(10, 20))
print(get_sum(10, 20, 30))

# ❷ 기본값 매개변수 예
def introduce(name="민수", age=20):
    print(f"이름은 {name}, 나이는 {age}세")
introduce()
introduce("지수")
introduce("지수", 21)