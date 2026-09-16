# ❶ 리스트(이터러블) 안에 짝을 이룬 데이터가 있을 때
my_list = [("name", "민수"), ("age", 20)]
#my_list = [["name", "민수"], ["age", 20]]
my_dict = dict(my_list)
print(my_dict)

# ❷ 튜플(이터러블) 안에 짝을 이룬 데이터가 있을 때
# 튜플은 내용물을 바꿀 수 없어 더 안전한 보관함
my_tuple = (["name", "민수"], ["age", 20])
#my_tuple = (("name", "민수"), ("age", 20))
my_dict = dict(my_tuple)
print(my_dict)

# ❸ 직접 키와 값을 지정하기 (키워드 방식)
# 변수를 만들듯 '키=값' 형태로 나열하는 가장 직관적인 방법
my_dict = dict(name="민수", age=20)
print(my_dict)

# ❹ 기존 데이터에 새로운 정보 추가 (혼합 방식)
my_list = [("name", "민수"), ("age", 20)]
my_dict = dict(my_list, city="서울")
print(my_dict)

# ❺ zip()(→9.2.5절)으로 두 리스트 묶은 후 딕셔너리로 변환
keys = ["name", "age", "city"]
values = ["진우", 23, "부산"]
my_dict = dict(zip(keys, values))
print(my_dict)