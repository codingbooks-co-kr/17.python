# 이진 파일 쓰기 
with open("data.bin", "wb") as file:
    file.write(b"Hello Python")

# 이진 파일 읽기
with open("data.bin", "rb") as file:
    content = file.read()
    print(content, type(content))