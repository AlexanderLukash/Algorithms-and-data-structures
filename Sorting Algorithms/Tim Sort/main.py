def InsertionSort(nums: list[int], left: int, right: int) -> list[int]:
    for i in range(left + 1, right + 1):
        j = i
        while j > left and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1

def merge(nums: list[int], left: int, mid: int, right: int) -> list[int]:
    ll = nums[left:mid+1]
    rl = nums[mid+1:right+1]

    i = 0
    j = 0
    k = left

    while i < len(ll) and j < len(rl):
        if ll[i] <= rl[j]:
            nums[k] = ll[i]
            i += 1
        else:
            nums[k] = rl[j]
            j += 1
        k += 1

    while i < len(ll):
        nums[k] = ll[i]
        i += 1
        k += 1

    while j < len(rl):
        nums[k] = rl[j]
        j += 1
        k += 1


def compute_min_run(n):
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r

def TimSort(nums: list[int]) -> list[int]:
    n = len(nums)
    min_run = compute_min_run(n)

    for start in range(0, n, min_run):
        end = min(start+min_run - 1, n-1)
        InsertionSort(nums, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(left + size - 1, n-1)
            right = min(left + 2 * size - 1, n - 1)

            if mid < right:
                merge(nums, left, mid, right)

        size *= 2

    return nums



if __name__ == '__main__':
    print(TimSort(
        [3, 1, 2, 5, 4, 6, 8, 7, 10, 9, 2, -2, 4, 5, 12, 4, 0, 1, 3, 1, 2, 5, 4, 6, 8, 7, 10, 9, 2, -2, 4, 5, 12, 4, 0,
         1, 3, 1, 2, 5, 4, 6, 8, 7, 10, 9, 2, -2, 4, 5, 12, 4, 0, 1, 3, 1, 2, 5, 4, 6, 8, 7, 10, 9, 2, -2, 4, 5, 12, 4,
         0, 1]))
    print(TimSort([5, 3, 8, 8, 4, 1]))
