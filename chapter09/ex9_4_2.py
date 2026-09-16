# ❷ 세 개의 리스트에 map() 함수를 적용한 예
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

# 세 리스트의 요소별 덧셈 변환
result = map(lambda x, y, z: x+y+z, nums1, nums2, nums3)
print(list(result))