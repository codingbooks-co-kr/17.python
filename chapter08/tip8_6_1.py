my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# ❶ 키(Key) 확장 언패킹 (중간 키들을 리스트로 묶기)
first, *middle, last = my_dict
print(first, middle, last)

# ❷ 값(Value) 확장 언패킹 (중간 값들을 리스트로 묶기)
first, *middle, last = my_dict.values()
print(first, middle, last)

# ❸ (키, 값) 쌍 확장 언패킹 (중간 항목들을 리스트로 묶기)
first, *middle, last = my_dict.items()
print(first, middle, last)