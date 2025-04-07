def InsertionSort(nums: list[int]) -> list[int]:
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


def BucketSort(nums: list[float | int]) -> list[float | int]:
    n = len(nums)
    buckets = [[] for _ in range(n)]

    for num in nums:
        bi = int(n * num)
        buckets[bi].append(num)

    for bucket in buckets:
        InsertionSort(bucket)

    i = 0
    for bucket in buckets:
        for num in bucket:
            nums[i] = num
            i += 1

    return nums


if __name__ == "__main__":
    print(BucketSort([0.5, 0.3, 0.4, 0.1]))
    print(BucketSort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]))
