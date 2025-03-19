def heapify(nums: list[int], length: int, index: int):
    largest = index

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < length and nums[left_index] > nums[largest]:
        largest = left_index

    if right_index < length and nums[right_index] > nums[largest]:
        largest = right_index

    if largest != index:
        nums[index], nums[largest] = nums[largest], nums[index]
        heapify(nums, length, index)


def HeapSort(nums: list[int]) -> list[int]:
    length = len(nums)

    for i in range(length // 2 - 1, -1, -1):
        heapify(nums, length, i)

    for i in range(length - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)

    return nums


if __name__ == '__main__':
    print(HeapSort([5, 3, 8, 8, 4, 1]))

