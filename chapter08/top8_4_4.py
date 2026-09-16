# ❽ 리스트(또는 튜플) → 문자열 (모든 요소가 문자열일 때)
my_list = ['P', 'y', 't', 'h', 'o', 'n']
result = "".join([*my_list])
print(result)

# ❾ 세트(순서보장 없고 중복요소 제거) → 문자열(모든 요소가 문자열일 때)
my_set = {"red", "green", "blue", "red"}
result = "-".join([*my_set])
print(result)