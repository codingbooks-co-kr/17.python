# 몫과 나머지 계산 응용-1
# 초를 입력받아 분/초 계산

sec = 456		# 456초

minute = sec // 60		# 몫: int(sec/60)
second = sec % 60	# 나머지

print("입력:", sec, "초")
print("출력:", minute, "분", second, "초")