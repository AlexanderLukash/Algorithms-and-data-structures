def heapify(nums: list[int], length: int, index: int):
    largest = index

    l = 2 * index + 1
    r = 2 * index + 2

    if l < length and nums[l] > nums[largest]:
        largest = l

    if r < length and nums[r] > nums[largest]:
        largest = r

    if largest != index:
        nums[index], nums[largest] = nums[largest], nums[index]
        heapify(nums, length, largest)


def HeapSort(nums: list[int]) -> list[int]:
    n = len(nums)

    for i in range(n // 2-1, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
    return nums


if __name__ == '__main__':
    print(HeapSort([5, 3, 8, 8, 4, 1]))


