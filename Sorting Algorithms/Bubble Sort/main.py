def BubbleSortWhile(nums: list[int]) -> list[int]:
    length = len(nums) - 1
    max_index = 0
    while length != 0:
        for i in range(length):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                max_index = i
        length = max_index
    return nums


def BubbleSortFor(nums: list[int]) -> list[int]:
    length = len(nums) - 1

    for i in range(length):
        for j in range(length - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


if '__main__' == __name__:
    print(BubbleSort([5, 3, 8, 4, 1]))

    print(BubbleSortWhile([5, 3, 8, 4, 1]))

    print(BubbleSortFor([5, 3, 8, 4, 1]))
