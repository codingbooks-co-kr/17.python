# ❷ if문으로 특정 문자(열) 포함 여부 확인 

words = "Good Morning Python"
keyword = "Python" 

if keyword in words:
    print(f"문자열에 '{keyword}' 있음")
else:
    print(f"문자열에 '{keyword}' 없음")