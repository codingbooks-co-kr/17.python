my_set = {1, 2, 3}

# 요소 추가: add()
my_set.add(4)		# 새 요소(4) 추가
print(my_set)

my_set.add(2)		# 요소(2)의 중복 허용 불가!
print (my_set)

# 여러 요소 추가(다른 이터러블 사용): update()
my_set.update([3, 4, 5])	# 리스트로 여러 개 추가
print(my_set)
my_set.update({5, 6, 7})	# 세트로 여러 개 추가
print(my_set)

# 요소 제거-1: remove()
my_set.remove(5)		# 요소(5) 제거
#my_set.remove(10)		# 없는 요소 제거 시 오류!
print(my_set)

# 요소 제거-2: discard()
my_set.discard(6)		# 요소(6) 제거
print(my_set)
my_set.discard(10)		# 없는 요소 제거 시 오류 없음!
print (my_set)

# 임의의 요소 제거: pop() (→어떤 요소가 제거될지 모름)
# 빈 세트에서 pop 호출 시 오류 발생
if my_set:			# 세트가 비어있는지 확인
    removed_item = my_set.pop()
    print(f"pop으로 제거된 요소: {removed_item}")
    print(f"pop 후 세트: {my_set}")

# 모든 요소 제거: clear()
my_set.clear()
print(my_set)