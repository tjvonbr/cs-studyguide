"""
Implement next permutation, which arranges numbers
into the lexicographically next greater permutation of
numbers.  If such an arrangement is not possible, it must
rearrange it as the lowest possible order.
"""

def permute(nums: list[int]) -> None:
    m = len(nums)
    output = []

    def backtrack(first = 0):
        if first == m:
            output.append(nums[:])
        for i in range(first, m):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    backtrack()

    return output

print(permute([1, 2, 3]))
