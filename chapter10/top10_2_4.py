# 이미지 파일 복사의 예
with open("image.png", "rb") as src:          # 원본 읽기
    data = src.read()
with open("image2.png", "wb") as src_copy:   # 복사본 쓰기
    src_copy.write(data)
print("이미지 파일 복사 완료!")