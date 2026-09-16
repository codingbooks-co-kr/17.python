my_dict = {"a": 1, "b": 2, "c": 3}
print(*my_dict)		  # ❶ 키만 언패킹-1
print(*my_dict.keys())	  # ❷ 키만 언패킹-2
#print(**my_dict)		  # ❸ 오류!

new_dict = {**my_dict, "d": 4}	  # ❹ 키:값 모두 언패킹
print(new_dict)