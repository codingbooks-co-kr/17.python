# ❸ 문자열 → 리스트
result = [*"banana"]		# 시퀀스 병합의 특수한 형태
print(result)

# ❹ 문자열 → 튜플 (튜플은 괄호() 생략 가능하지만 콤마(,)는 필수)
result = (*"banana",)		# 괄호생략가능: result = *"banana",
print(result)

# ❺ 리스트 → 튜플 (튜플은 괄호() 생략 가능하지만 콤마(,)는 필수)
my_list = [1, 2, 2, 3]	# 리스트
result = (*my_list,)		# 괄호생략가능: result = *my_list,
print(result)

# ❻ 문자열 → 세트 (순서 보장 없고 중복 요소 제거)
result = {*"banana"}		# 문자열
print(result)

# ❼ 리스트(또는 튜플) → 세트 (순서 보장 없고 중복 요소 제거)
my_list = [1, 2, 2, 3, "a", "b", "b"]	# 리스트
result = {*my_list}
print(result)