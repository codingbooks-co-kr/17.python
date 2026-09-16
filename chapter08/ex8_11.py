# ❶ (사용자정의)함수 호출 시 딕셔너리 언패킹(→키워드인수 전달)
def info1(name, age):	# 함수 정의
    print(name, age)
student = {"name": "민수", "age": 20}
info1(**student)		# 함수 호출 (딕셔너리언패킹)

# ❷ (사용자정의)함수 정의 시 딕셔너리 패킹(→가변키워드매개변수: 5.5절)
def info2(**kwargs):	   	# 함수 정의 (딕셔너리 패킹)
    print(kwargs)
info2(name="민수", age=20)  	# 함수 호출 (복수 개의 키워드 인수 전달)

# ❸ (사용자정의)함수 호출 시 딕셔너리 언패킹, 정의 시 딕셔너리 패킹
def info3(**kwargs):	   	# 함수 정의 (딕셔너리 패킹)
    print(kwargs)
student = {"name": "민수", "age": 20}
info3(**student)		# 함수 호출 (딕셔너리 언패킹)