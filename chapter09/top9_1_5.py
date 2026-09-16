# 메모리 사용량 차이를 보여주는 시뮬레이션

# ❶ 리스트 함축: 메모리상에 10,000개의 값을 한 번에 생성
import sys			# sys 모듈 불러오기
data1 = [x for x in range(10000)]	# 리스트 함축: 대괄호 []
print(sys.getsizeof(data1))	  	# data1 객체의 메모리 크기(바이트)

# ❷ 제너레이터 표현식: 메모리상에 필요할 때마다 값을 하나씩 생성
data2 = (x for x in range(10000))	# 소괄호 ()를 사용한 제너레이터 표현식
print(sys.getsizeof(data2))	  	# data2 객체의 메모리 크기(바이트)