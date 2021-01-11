def bubbleSort(nums):
    m = len(nums)

    for i in range(m-1):
        for j in range(i+1, m):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

    return nums

print(bubbleSort([5, 3, 2, 6, 7]))
