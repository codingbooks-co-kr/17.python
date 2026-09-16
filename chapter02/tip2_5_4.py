result1, result2 = divmod(10, 3)	# ❶튜플 언패킹 (→[심화7.2] 참조) 
print("몫:", result1, "나머지:", result2)

result = divmod(10, 3)		# ❷튜플 인덱싱 (→[심화7.2] 참조)
print("몫:", result[0], "나머지:", result[1])