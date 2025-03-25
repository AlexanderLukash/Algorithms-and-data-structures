def ShellSort(nums: list[int]) -> list[int]:
    length = len(nums)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap //=2

    return nums



if __name__ == '__main__':
    print(ShellSort([5, 3, 8, 8, 4, 1]))
