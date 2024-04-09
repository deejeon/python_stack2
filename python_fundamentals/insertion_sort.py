def insertion_sort(nums):
    if len(nums) <= 1:
        return nums
    for i in range(1, len(nums)):
        to_insert = nums[i]
        j = i - 1
        while (j >= 0 and to_insert < nums[j]):
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = to_insert
    return nums



print(insertion_sort([10,9,7,8]))