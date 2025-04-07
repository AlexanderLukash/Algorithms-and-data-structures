def ShellSort(nums: list[int]) -> list[int]:
    n = len(nums)

    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap //= 2

    return nums

if __name__ == '__main__':
    print(ShellSort([5, 3, 8, 8, 4, 1]))
