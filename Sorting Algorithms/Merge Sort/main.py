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


def mergeSort(arr, l, r):
    # code here
    n = len(arr)
    if n > 1:
        ll = arr[:n // 2]
        rl = arr[n // 2:]

        mergeSort(ll, l, r)
        mergeSort(rl, l, r)

        i = 0
        j = 0
        k = 0

        while i < len(ll) and j < len(rl):
            if ll[i] <= rl[j]:
                arr[k] = ll[i]
                i += 1
            else:
                arr[k] = rl[j]
                j += 1
            k += 1

        while i < len(ll):
            arr[k] = ll[i]
            i += 1
            k += 1

        while j < len(rl):
            arr[k] = rl[j]
            j += 1
            k += 1

        return arr


if __name__ == '__main__':
    print(MergeSort([5, 3, 8, 8, 4, 1]))
    print(mergeSort([5, 3, 8, 8, 4, 1], 0, len([5, 3, 8, 8, 4, 1])))
