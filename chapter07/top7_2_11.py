# 일반적인 출력 vs 언패킹 출력
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)	# 튜플을 '통째로' 출력
print(*my_tuple)	# 함수 호출 시 튜플을 '풀어서'(언패킹) 출력

# (사용자정의)함수 정의 시 튜플 패킹 (→가변위치매개변수: 5.5절)
def func(*args): 	  	# 함수정의 시 튜플 패킹
    print(args)	  	# 튜플을 '통째로' 출력
func(1, 2, 3, 4, 5)  	# 함수호출(복수 개의 위치 인수 전달)

# 함수에서 여러 값을 튜플로 패킹하여 반환 (→[질문5.12] 참조)
def info():			# 함수정의
    name = "민수"
    age = 20
    return name, age 	# 튜플 패킹
name, age = info()	  	# 함수호출 (튜플 언패킹)
print(name, age)