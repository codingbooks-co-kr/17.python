# 여러 종류의 매개변수를 함께 사용한 예
def print_values(a, b=0, *args, c, **kwargs):
    print("위치매개변수:", a)
    print("기본값매개변수:", b)
    print("가변위치매개변수:", args)	# 튜플(심화7.2)
    print("키워드매개변수:", c)
    print("가변키워드매개변수:", kwargs)	# 딕셔너리(8장)

print_values(1, 2, 3, 4, c=5, x=10, y=20)