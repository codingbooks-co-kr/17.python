# (4) Built-in(내장 스코프): 파이썬의 내장 함수(예: print, input 등), 자료형, 예외 이름, 시스템 변수
# (3) Global(전역 스코프): 파일 최상단에 정의된 변수
x = "전역변수(Global)"

def outer_function():
    # (2) Enclosing(바깥 스코프): 나를 감싸고 있는 바깥 함수의 변수
    x = "바깥변수(Enclosing)"
  
    def inner_function():
        # (1) Local(지역 스코프): 현재 내가 있는 함수 안의 변수
        x = "지역변수(Local)"
        print(f"지금 찾는 x는? => {x}") 
    inner_function()		# ❷ 안쪽 함수 호출

outer_function()		# ❶ 바깥쪽 함수 호출