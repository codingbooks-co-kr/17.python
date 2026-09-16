# 함수에서 리스트 반환

def get_info():	 	# x,y 좌표를 리스트로 반환
    x = 10
    y = 20
    return [x, y]		# 리스트 반환

info = get_info()	 	# 반환값(리스트)를 변수에 저장
print(get_info())	 	# 반환값(리스트) 확인
print(f"x좌표: {info[0]}, y좌표: {info[1]}")