def CountingSort(nums: list[int]) -> list[int]:
    n = len(nums)
    max_value = max(nums)
    output = [0] * n
    count = [0] * (max_value + 1)

    for num in nums:
        count[num] += 1

    for i in range(1, max_value+1):
        count[i] += count[i-1]

    for i in range(n):
        output[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -= 1

    return output
if __name__ == '__main__':
    print(CountingSort([5, 3, 8, 4, 1]))
