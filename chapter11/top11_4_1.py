# id(): 객체의 고유한 식별자를 반환
x = 10
y = 10
print(id(x))			# 객체(x)의 고유 ID
print(id(y))			# 객체(y)의 고유 ID
print(id(x) == id(y))		# x, y는 동일 객체, 또는 print(x is y)