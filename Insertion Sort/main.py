def InsertionSort(nums: list[int]) -> list[int]:
    length = len(nums)

    for step in range(1, length):
        key = nums[step]
        j = step - 1

        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1

        nums[j + 1] = key

    return nums

if '__main__' == __name__:
    print(InsertionSort([5, 3, 8, 4, 1]))
