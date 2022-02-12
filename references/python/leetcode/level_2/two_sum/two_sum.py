nums = [2, 7, 11, 15]


"""
Official best answer
"""
def two_sum(nums,target):
    mapping = {}
    for i, num in enumerate(nums):
        mapping[num] = i
        if target - num in mapping:
            return i, mapping[target - num]
print(two_sum(nums,9))
print(two_sum(nums,26))
print(two_sum(nums,18))
print(two_sum(nums,17))
print(two_sum(nums,22))