# 텍스트 파일 쓰기
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")

# 텍스트 파일 읽기
with open("data.txt", "r") as file:
    content = file.read()
    print(content, type(content))