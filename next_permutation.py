"""
Implement next permutation, which arranges numbers
into the lexicographically next greater permutation of
numbers.  If such an arrangement is not possible, it must
rearrange it as the lowest possible order.
"""

def nextPermutation(nums: list[int]) -> None:
    # Do not return anything, modify nums in place
    m = len(nums)

    for i in range(m-1):
        print(nums)
        for j in range(1, m):
            nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[j] = nums[j], nums[i]

print(nextPermutation([1, 2, 3]))
