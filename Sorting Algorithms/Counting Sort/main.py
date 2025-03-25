def CountingSort(nums: list[int]) -> list[int]:
    length = len(nums)

    max_value = max(nums)
    count = [0] * (max_value + 1)

    for num in nums:
        count[num] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    output_array = [0] * length
    for i in range(length - 1, -1, -1):
        output_array[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -= 1

    return output_array


if __name__ == '__main__':
    print(CountingSort([5, 3, 8, 8, 4, 1]))
