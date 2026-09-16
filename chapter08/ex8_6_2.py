# ❷ 키 입력을 통한 데이터 조회 (안전한 검색)

student = {"name": "민수", "age": 20}
search_key = input("키 입력: ")
if search_key in student:
    print(f"조회 성공! {search_key}: {student[search_key]}")
else:
    print(f"조회 실패! '{search_key}'에 대한 정보는 없음")