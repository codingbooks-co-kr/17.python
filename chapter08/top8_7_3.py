# 함수에서 딕셔너리 반환

def get_info():		# 세 정보를 딕셔너리로 반환
    name = "민수"
    age = 20
    major = "컴퓨터공학"
    return {"이름": name, "나이": age, "전공": major}

student = get_info()		# 반환값(딕셔너리)을 변수에 저장
print(get_info())		# 반환값(딕셔너리) 확인
print(f"이름은 {student['이름']}입니다")
print(f"나이는 {student['나이']}세입니다")
print(f"전공은 {student['전공']}입니다")