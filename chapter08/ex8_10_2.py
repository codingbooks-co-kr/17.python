# ❸ ** 연산자로 딕셔너리 언패킹 후 병합-1(키 중복 시 뒤의 값 우선)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"d": 5, "e": 6}
result = {**dict1, **dict2, **dict3}
print(result)

# ❹ ** 연산자로 딕셔너리 언패킹 후 병합-2(키 중복 시 뒤의 값 우선)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
result = {**dict1, **dict2, "d": 5}
print(result)