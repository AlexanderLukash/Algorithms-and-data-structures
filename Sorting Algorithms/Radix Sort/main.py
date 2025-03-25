def CountingSort(nums: list[int], exp: int) -> list[int]:
    length = len(nums)

    output_array = [0] * length
    count = [0] * 10

    for i in range(length):
        index = nums[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = length - 1
    while i >= 0:
        index = nums[i] // exp
        output_array[count[index % 10] - 1] = nums[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(length):
        nums[i] = output_array[i]

    return nums


def RadixSort(nums: list[int]) -> list[int]:
    max_value = max(nums)

    exp = 1
    while max_value // exp >= 1:
        CountingSort(nums, exp)
        exp *= 10

    return nums


if __name__ == '__main__':
    print(RadixSort([170, 45, 75, 90, 802, 24, 2, 66]))
    print(RadixSort([5, 3, 8, 8, 4, 1]))
