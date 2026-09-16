# ❶ 가변 위치 매개변수(*args)
# 여러 개의 위치 인수를 튜플(심화7.2)로 묶기

def print_score(*scores):
    print(scores, type(scores))		# 튜플
    for score in scores:
        print(f"점수: {score}점")

print_score(88, 92, 75)