def InsertionSort(nums: list[int], left: int, right: int) -> list[int]:
    length = len(nums)

    for step in range(left + 1, right + 1):
        key = nums[step]
        j = step - 1

        while j >= left and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums


def MergeSort(nums: list[int], left: int, mid: int, right: int) -> list[int]:
    len_1, len_2 = mid - left, right - mid

    left_list = nums[:len_1]
    right_list = nums[len_2:]

    left_list_index = 0
    right_list_index = 0
    merged_list_index = left

    while left_list_index < len_1 and right_list_index < len_2:
        if left_list[left_list_index] < right_list[right_list_index]:
            nums[merged_list_index] = left_list[left_list_index]
            left_list_index += 1
        else:
            nums[merged_list_index] = right_list[right_list_index]
            right_list_index += 1
        merged_list_index += 1

    while left_list_index < len_1:
        nums[merged_list_index] = left_list[left_list_index]
        left_list_index += 1
        merged_list_index += 1

    while right_list_index < len_2:
        nums[merged_list_index] = right_list[right_list_index]
        right_list_index += 1
        merged_list_index += 1

    return nums


def TimSort(nums: list[int]) -> list[int]:
    length = len(nums)

    min_run = length // 2

    for start in range(0, length, min_run):
        end = min(start + min_run - 1, length - 1)
        InsertionSort(nums, start, end)

    size = min_run
    while size < length:
        for i in range(0, length, size * 2):
            mid = i + size - 1
            end = min((i + size * 2 - 1), length - 1)

            if mid < end:
                MergeSort(nums, i, mid, end)
        size *= 2

    return nums


if __name__ == '__main__':
    print(TimSort([5, 3, 8, 8, 4, 1]))
