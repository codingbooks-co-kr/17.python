# 지역변수와 전역변수

num = 100		# 함수 밖에서 정의된 전역변수

def func1():		# 함수1
    print(num)		# ❷100 (함수 안에 num이 없어 밖의 전역변수를 읽어옴)

def func2():		# 함수2
    global num		# 함수 안에서 전역변수 num을 직접 수정하겠다고 선언
    num = 200		# 전역변수 값 자체가 200으로 변경됨
    print(num)		# ❸200

def func3():		# 함수3
    num = 300		# 전역변수와 이름만 같을 뿐, 새로운 지역변수 num을 생성
    print(num)		# ❹300

# --- 메인 코드 실행 ---
print(num)			# ❶100 (처음 설정된 전역변수 값 출력)
func1()
func2()
func3()
print(num)			# ❺200 (func2에서 전역변수가 200으로 바뀌었음을 확인)

for x in range(3):		# 파이썬에서 for문 내부의 변수는 전역변수 (x = 0, 1, 2)
    num += 10		# num=num+10, 여기서 num은 전역변수
    print(num, end=" ")	# ❻210 220 230

print()			# 개행(줄바꿈)
print(num, x)		# ❼230 2 (for문 종료 후 num과 x는 전역변수로 살아있음)