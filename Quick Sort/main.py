def partition(nums: list[int], lo: int, hi: int):
    pivot = nums[hi]
    i = lo - 1

    for j in range(lo, hi):
        if nums[j] < pivot:
            i += 1
            swap(nums, i, j)

    swap(nums, i + 1, hi)
    return i + 1


def swap(nums: list[int], i: int, j: int):
    nums[i], nums[j] = nums[j], nums[i]


def QuickSort(nums: list[int], lo: int, hi: int) -> list[int]:
    if lo < hi:
        pivot = partition(nums, lo, hi)
        QuickSort(nums, lo, pivot - 1)
        QuickSort(nums, pivot + 1, hi)

    return nums


if __name__ == '__main__':
    nums = [5, 3, 8, 8, 4, 1]
    print(QuickSort(nums, 0, len(nums) - 1))
