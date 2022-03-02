# Trapping rain water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example:
'''
              _
      _      | |_   _
  _  | |_   _|   |_| |_
_| |_|   |_|           |_
'''
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# A Simple Solution is to traverse every array element and find the highest bars on left and right sides. Take the smaller of two heights. The difference between the smaller height and height of the current element is the amount of water that can be stored in this array element. Time complexity of this solution is O(n2).
# An Efficient Solution is to pre-compute highest bar on left and right of every bar in O(n) time. Then use these pre-computed values to find the amount of water in every array element.
# Python program to find maximum amount of water that can
# be trapped within given set of bars.

from re import A


def find_water_simple(arr, n):

    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = [0]*n

    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = [0]*n

    # Initialize result
    water = 0

    # Initialize left array to first first element in input arr
    left[0] = arr[0]
    # Fill the rest of left array
    for i in range( 1, n):
        left[i] = max(left[i-1], arr[i])

    # Fill last element of right array with last element of input arr
    right[-1] = arr[-1]
    # Loops backwards starting from the second to last element of the right array to fill the rest of the right array.
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i],right[i]) - arr[i]

    return water

# Space Optimization in above solution: Instead of maintaining two arrays of size n for storing left and right max of each element, we will just maintain two variables to store the maximum till that point. Since water trapped at any element = min( max_left, max_right) – arr[i] we will calculate water trapped on smaller element out of A[lo] and A[hi] first and move the pointers till lo doesn’t cross hi.

def find_water_better(arr,n):

    # initialize output
    result = 0
    
    # maximum element on left and right
    left_max = 0
    right_max = 0
    
    # indices to traverse the array
    lo = 0
    hi = n-1
    
    while(lo <= hi):
        if(arr[lo] < arr[hi]):
            if(arr[lo] > left_max):
                # update max in left
                left_max = arr[lo]
            else:
                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo+=1
        
        else:
            if(arr[hi] > right_max):
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi-=1
        
    return result

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

input = [0,1,0,2,1,0,1,3,2,1,2,1]
length = len(input)

print(find_water_simple(input,length))
print(find_water_better(input,length))