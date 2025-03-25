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


def quicksort(nums: list[int], lo: int, hi: int) -> list[int]:
    if lo < hi:
        pivot_index = partition(nums, lo, hi)

        quicksort(nums, lo, pivot_index - 1)
        quicksort(nums, pivot_index + 1, hi)

    return nums

nums = [5, 3, 8, 8, 4, 1]
n = len(nums)
print(quicksort(nums, 0, n - 1))
