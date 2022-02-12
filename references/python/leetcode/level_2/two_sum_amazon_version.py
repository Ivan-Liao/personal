nums = [2, 7, 11, 15]


"""
Official best answer
"""


def two_sum(nums, target):
    p1,p2= 0, len(nums) - 1

    while p1 < p2:
        curSum = nums[p1] + nums[p2]

        if curSum > target:
           p2-= 1
        elif curSum < target:
            p1+= 1
        else:
            return [p1+1,p2+1]


print(two_sum(nums, 9))
print(two_sum(nums, 26))
print(two_sum(nums, 18))
print(two_sum(nums, 17))
print(two_sum(nums, 22))
