# ❶ 위치 매개변수
def introduce(name, age):
    print(f"이름은 {name}이고 나이는 {age}세입니다.")
introduce("민수", 20)

# ❷ 키워드 매개변수 (매개변수의 순서를 바꿔도 됨)
def introduce(name, age):
    print(f"이름은 {name}이고 나이는 {age}세입니다.")
introduce(age=20, name="민수")
introduce(name="민수", age=20)

# ❸ 위치/키워드 매개변수를 함께 사용 시 위치 매개변수가 먼저 옴
def introduce(name, age):
    print(f"이름은 {name}이고 나이는 {age}세입니다.")
introduce("민수", age=20)		# 정상!
# introduce(name="민수", 20)		# 오류!