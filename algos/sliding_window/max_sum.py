"""
Max sum with positive integers only
"""

def max_sum(nums, k):
    max_sum = 0

    for i in range(len(nums) - (k - 1)):
        if sum(nums[i:i+k]) > max_sum:
            max_sum = sum(nums[i:i+k])

    return max_sum

"""
Still need to work on some corner cases for this algo
"""
