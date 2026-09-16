# ❶ (내장)함수인 print() 호출 시 문자열 언패킹(풀기)
word = "Python"
print(*word)		# print() 함수 호출 시 문자열 언패킹

# ❷ (사용자정의)함수 호출 시 문자열 언패킹(풀기)
def func1(a, b, c, d, e, f):   	# 함수 정의(→위치매개변수: 5.5절)
    print(a, b, c, d, e, f)
word = "Python"
func1(*word)		# 함수 호출 시 문자열 언패킹

# ❸ (사용자정의)함수 호출 시 문자열 언패킹(풀기) → 정의 시 패킹(묶기)
def func2(*args):   	# 함수 정의 시 튜플패킹(→가변위치매개변수: 5.5절)
    print(args)	# 튜플 출력
word = "Python"
func2(*word)	# 함수 호출 시 문자열 언패킹