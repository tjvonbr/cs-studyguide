def selectionSort(nums):
    m = len(nums)

    for i in range(m):
        smallest_idx = i

        for j in range(i + 1, m):
            if nums[smallest_idx] > nums[j]:
                smallest_idx = j

        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]

    return nums

print(selectionSort([5, 3, 6, 2, 7]))

[2, 3, 6, 5, 7]
smallest_num = 3
smallest_idx = 1