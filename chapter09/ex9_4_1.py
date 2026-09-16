# ❶ 길이가 다른 두 개의 리스트에 map() 함수를 적용한 예
nums1 = [1, 2, 3, 4, 5]
nums2 = [10, 20, 30]

# 람다 함수가 x(nums1에서 추출), y(nums2에서 추출) 두 개를 받음
result = map(lambda x, y: x + y, nums1, nums2)

# nums1의 4, 5는 짝이 없어서 무시됨
print(list(result))