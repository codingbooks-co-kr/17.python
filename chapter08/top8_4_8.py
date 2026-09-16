# ❺ 함수정의: *args는 튜플 패킹, **kwargs는 딕셔너리 패킹
def order(*args, **kwargs):	  # 함수 정의 시 패킹
    print(f"주문: {args}")
    print(f"요청: {kwargs}")

# 함수호출1: 앞의 2개는 튜플 전달, 뒤의 2개는 딕셔너리 전달
order("아메리카노", "레몬차", syrup="바닐라", ice="많이")

# 함수호출2: *my_choice 및 **my_request는 각각 언패킹
my_choice = ["아메리카노", "레몬차"]
my_request = {"syrup": "바닐라", "ice": "많이"}
order(*my_choice, **my_request)