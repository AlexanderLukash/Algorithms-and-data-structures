def InsertionSort(nums: list[int]) -> list[int]:
    lenght = len(nums)
    for i in range(1, lenght):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums


def BucketSort(nums: list[float | int]) -> list[float | int]:
    length = len(nums)

    buckets = [[] for _ in range(length)]
    for num in nums:
        bi = int(length * num)
        buckets[bi].append(num)

    for bucket in buckets:
        InsertionSort(bucket)
    index = 0
    for bucket in buckets:
        for num in bucket:
            nums[index] = num
            index += 1

    return nums


if __name__ == "__main__":
    print(BucketSort([0.5, 0.3, 0.4, 0.1]))
