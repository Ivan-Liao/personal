nums = [2, 7, 11, 15]


"""
Official best answer
"""


def two_sum(nums, target):
    mapping = {}
    for i, num in enumerate(nums):
        if (target - num) in mapping and num != (target - num):
            return [i, mapping[target - num]]
        mapping[num] = i


print(two_sum(nums, 9))
print(two_sum(nums, 26))
print(two_sum(nums, 18))
print(two_sum(nums, 17))
print(two_sum(nums, 22))
