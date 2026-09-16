# 함수에서 튜플 반환

def get_info():		# 이름/나이를 튜플로 반환
    name = "민수"
    age = 20
    return name, age	# 또는 return (name, age)

name, age = get_info()	# 반환값(튜플)을 변수에 할당
print(get_info())		# 반환값(튜플) 확인
print(f"이름: {name}, 나이: {age}")