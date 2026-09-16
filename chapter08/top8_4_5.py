# ❶ (내장)함수인 print() 호출 시 언패킹
print(*"Python")		# 내장함수 호출 시 문자 언패킹
print(*[1, 2, 3])		# 내장함수 호출 시 리스트/튜플 언패킹

# ❷ (사용자정의)함수 호출 시 언패킹, 정의 시 튜플 패킹
def func(*args):			# 함수 정의 시 패킹
    print(args)

my_word = "abc"			# 문자열
my_list = [1, 2, 3]			# 리스트
my_tuple = (4, 5)			# 튜플
func(*my_word, *my_list, *my_tuple)	# 함수 호출 시 언패킹