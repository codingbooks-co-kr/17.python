# UTF-8로 인코딩하여 바이트 객체로 변환
text = "파이썬".encode('utf-8')

# 이진 파일 쓰기
with open("data.bin", "wb") as file:
    file.write(text)

# 이진 파일 읽기
with open("data.bin", "rb") as file:
    content = file.read() 			# 파일 전체 읽기

print(content, type(content))			# 읽은 바이트 객체
decoded_content = content.decode('utf-8')	# 읽은 바이트 객체를 다시 문자열로 디코딩
print(decoded_content, type(decoded_content))