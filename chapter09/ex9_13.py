import datetime			# datetime 모듈 불러오기

# ❶ 현재 날짜만 표시
today = datetime.date.today()
print(f"현재 날짜: {today}")

# ❷ 현재 날짜와 시각 표시
now = datetime.datetime.now()
print(f"현재 시각: {now}")

# ❸ 현재 날짜와 시각 형식 지정
now2 = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초 %p %A")
print(f"현재 시각: {now2}")

# ❹ 오늘로부터 100일 후의 날짜 계산
date_change = today + datetime.timedelta(days=100)
print(f"100일 후 날짜: {date_change}")

# 오늘로부터 2주일 후의 날짜 계산
date_change = today + datetime.timedelta(weeks=2)
print(f"2주 후 날짜: {date_change}")

# 현재로부터 3시간 전 시간 계산
hour_change = now - datetime.timedelta(hours=3)
print(f"3시간 전 시각: {hour_change}")

# 현재로부터 특정 시간 후의 시간 계산
time_change = now + datetime.timedelta(days=2, hours=2, minutes=2, seconds=2)
print(f"2일 2시간 2분 2초 후: {time_change}")

# ❺ 날짜/시간 형식 지정
time_change2 = time_change.strftime("%Y년 %m월 %d일 %H시 %M분 %S초 %p %A")
print(f"변경 시각: {time_change2}")

# ❻ 특정 날짜 생성
specific_date = datetime.date(2026, 12, 31)
print(f"특정 날짜: {specific_date}")

# ❼ 특정 시각 생성
my_time = datetime.time(15, 30, 55)
print(f"특정 시각: {my_time}")

# ❽ 특정 날짜와 시각 생성
specific_time = datetime.datetime(2026, 12, 31, 15, 30, 55)
print(f"특정 시각: {specific_time}")

# ❾ 현재 시각과 특정 시각 사이의 차이
diff = specific_time - now
print(f"시간 차이: {diff}")		# timedelta 객체 반환
print(f"잔여 일수: {diff.days}일")		# timedelta 객체에서 전체 일수(정수)만 가져옴
print(f"시간 차이: {diff.total_seconds()}초")	# timedelta 객체에서 전체 초(실수)만 가져옴