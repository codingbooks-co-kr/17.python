# 불변 객체 (예: 정수)

num1 = 10	# num1은 정수 객체(10) 참조
print("num1:", num1, id(num1))

num1 = 20	# num1은 새로운 정수 객체(20) 참조
print("num1:", num1, id(num1))

num2 = num1	# num2는 num1과 동일한 객체 참조
print("num2:", num2, id(num2))

num1 = 30	# num1은 새로운 정수 객체(30) 참조
print("num1:", num1, id(num1))
print("num2:", num2, id(num2))