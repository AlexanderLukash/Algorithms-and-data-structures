def partition(nums: list[int], lo: int, hi: int) -> int:
    pivot = nums[hi]
    i = lo - 1

    for j in range(lo, hi):
        if nums[j] < pivot:
            i += 1
            swap(nums, i, j)

    swap(nums, i + 1, hi)

    return i + 1


def swap(array: list, i: int, j: int) -> list:
    array[i], array[j] = array[j], array[i]
    return array


def QuickSort(nums: list[int], lo: int, hi: int) -> list[int]:
    if lo < hi:
        pivot_index = partition(nums, lo, hi)

        QuickSort(nums, lo, pivot_index - 1)
        QuickSort(nums, pivot_index + 1, hi)

    return nums


if __name__ == '__main__':
    nums = [5, 3, 8, 8, 4, 1, 0, 10, 32, 1, 34, 2]
    print(QuickSort(nums, 0, len(nums) - 1))
