def MergeSort(nums: list[int]) -> list[int]:
    length = len(nums)
    if length > 1:
        left_list = nums[:length // 2]
        right_list = nums[length // 2:]

        MergeSort(left_list)
        MergeSort(right_list)

        left_list_index = 0
        right_list_index = 0
        merged_list_index = 0

        while left_list_index < len(left_list) and right_list_index < len(right_list):
            if left_list[left_list_index] < right_list[right_list_index]:
                nums[merged_list_index] = left_list[left_list_index]
                left_list_index += 1
            else:
                nums[merged_list_index] = right_list[right_list_index]
                right_list_index += 1
            merged_list_index += 1

        while left_list_index < len(left_list):
            nums[merged_list_index] = left_list[left_list_index]
            left_list_index += 1
            merged_list_index += 1

        while right_list_index < len(right_list):
            nums[merged_list_index] = right_list[right_list_index]
            right_list_index += 1
            merged_list_index += 1

    return nums


if __name__ == '__main__':
    print(MergeSort([5, 3, 8, 8, 4, 1]))
