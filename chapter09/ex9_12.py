import random		# random 모듈 불러오기

# ❶ seed(): 동일한 시드(seed 예: 0)를 주면 항상 같은 난수가 출력!
random.seed(0)		# 시드(seed) 설정

# ❷ random(): 0.0∼1.0 미만의 랜덤 실수 생성 (1.0 미포함)
print(random.random())	# 0.0∼1.0
print(random.random()*100)	# 0.0∼100.0

# ❸ uniform(a, b): a∼b 사이의 랜덤 실수 생성 (a와 b를 포함)
print(random.uniform(1.0, 10.0))

# ❹ randint(a, b): a∼b 사이의 랜덤 정수 생성 (a와 b를 포함)
print(random.randint(1, 10))

# ❺ choice(): 리스트/튜플/문자열에서 랜덤 요소 1개 선택
country = ["한국", "일본", "미국", "중국"]
print(random.choice(country))
print(random.choice("Python"))

# ❻ choices(): 리스트/튜플/문자열에서 3개 요소 추출 후 리스트로 반환(중복허용)
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(random.choices(nums, k=3))

# ❼ sample(): 리스트/튜플/문자열에서 3개 요소 추출 후 리스트로 반환(중복없음)
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(random.sample(nums, k=3))

# ❽ shuffle(): 리스트의 요소 순서를 무작위 섞기(원본 리스트 변경, 반환값:None)
cards = ['A', 'B', 'C', 'D']
random.shuffle(cards)
print(cards)