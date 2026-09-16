# 중첩 딕셔너리: 사원번호(Key)를 알면 전체를 훑지 않아도 바로 정보를 찾음
employee_db = {
    "26001": {"name": "김철수", "level": "대리", "dept": "개발팀"},
    "26005": {"name": "이영희", "level": "부장", "dept": "홍보팀"},
    "26012": {"name": "박민수", "level": "과장", "dept": "인사팀"}
}

# 사원번호로 검색 (반복문 없이 즉시 접근)
emp_id = "26005"
if emp_id in employee_db:
    emp_info = employee_db[emp_id]
    print(f"[사원번호: {emp_id}의 조회 결과]")
    print(f"이름: {emp_info['name']}, 직급: {emp_info['level']}, 부서: {emp_info['dept']}")
else:
    print(f"사원번호 {emp_id}를 찾을 수 없습니다.")