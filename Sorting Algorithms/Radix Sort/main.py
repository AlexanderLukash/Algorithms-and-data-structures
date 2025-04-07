def CountingSort(nums: list[int], exp: int) -> list[int]:
    n = len(nums)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = nums[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = nums[i] // exp
        output[count[index % 10] - 1] = nums[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        nums[i] = output[i]


def RadixSort(nums: list[int]) -> list[int]:
    max_value = max(nums)

    exp = 1
    while max_value // exp >= 1:
        for i in range(len(nums) - 1):
            CountingSort(nums, exp)
        exp *= 10
    return nums


if __name__ == '__main__':
    print(RadixSort([170, 45, 75, 90, 802, 24, 2, 66]))
    print(RadixSort([5, 3, 8, 8, 4, 1]))
