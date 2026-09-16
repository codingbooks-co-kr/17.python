# ❷ 가변 키워드 매개변수(**kwargs)
# 여러 개의 키워드 인수를 딕셔너리(8장)로 묶기

def print_score(**scores):
    print(scores, type(scores))		# 딕셔너리
    for subject, score in scores.items():
        print(f"{subject}: {score}점")

print_score(영어=80, 수학=92, 과학=78)