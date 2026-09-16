# 제너레이터 함수를 사용하여 제너레이터 객체(→이터레이터의 한 종류) 생성
def my_generator():		# 제너레이터 함수 정의
    yield 1  		# 값 1을 반환 후 함수의 실행을 일시 정지
    yield 2  		# 값 2를 반환 후 함수의 실행을 일시 정지
    yield 3  		# 값 3을 반환 후 함수의 실행을 일시 정지

my_gen = my_generator()	# 함수 호출 → 제너레이터 객체(my_gen) 생성
for num in my_gen:	# for 루프가 my_gen의 값을 하나씩 요청
    print(num)