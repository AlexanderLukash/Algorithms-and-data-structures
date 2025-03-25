def SelectionSort(nums: list[int]) -> list[int]:
    length = len(nums)

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if nums[min_index] > nums[j]:
                min_index = j

        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


if '__main__' == __name__:
    print(SelectionSort([5, 3, 8, 4, 1]))
