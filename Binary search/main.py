INF = 10 ** 9 + 7


def BinarySearchRec(nums: list[int], target: int, lo: int, hi: int) -> int | None:
    if lo > hi:
        return None

    mi = lo + (hi - lo) // 2
    if nums[mi] == target:
        return mi

    if nums[mi] < target:
        return BinarySearchRec(nums, target, mi + 1, hi)

    return BinarySearchRec(nums, target, lo, mi - 1)


def BinarySearch(nums: list[int], target: int) -> int | None:
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mi = lo + (hi - lo) // 2
        if nums[mi] == target:
            return mi
        elif nums[mi] < target:
            lo = mi + 1
        else:
            hi = mi - 1

    return None


def LowerBoundRec(nums: list[int], target, lo: int, hi: int) -> int | None:
    if lo > hi:
        return INF

    mi = lo + (hi - lo) // 2
    if nums[mi] < target:
        return LowerBoundRec(nums, target, mi + 1, hi)
    return min(mi, LowerBoundRec(nums, target, lo, mi - 1))


def LowerBound(nums: list[int], target: int) -> int:
    lo = 0
    hi = len(nums) - 1
    result = -1

    while lo <= hi:
        mi = lo + (hi - lo) // 2
        if nums[mi] < target:
            lo = mi + 1
        else:
            result = mi
            hi = mi - 1

    return result


def UpperBoundRec(nums: list[int], target: int, lo: int, hi: int) -> int:
    if lo > hi:
        return INF

    mi = lo + (hi - lo) // 2

    if nums[mi] <= target:
        return UpperBoundRec(nums, target, mi + 1, hi)
    return min(mi, UpperBoundRec(nums, target, lo, mi - 1))


def UpperBound(nums: list[int], target: int) -> int:
    lo = 0
    hi = len(nums) - 1
    result = -1

    while lo <= hi:
        mi = lo + (hi - lo) // 2
        if nums[mi] <= target:
            lo = mi + 1
        else:
            result = mi
            hi = mi - 1

    return result


def BinaryFirstRec(nums: list[int], target: int, lo: int, hi: int) -> int:
    if lo > hi:
        return INF

    mi = lo + (hi - lo) // 2

    if nums[mi] < target:
        return BinaryFirstRec(nums, target, mi + 1, hi)
    elif nums[mi] > target:
        return BinaryFirstRec(nums, target, lo, mi - 1)
    return min(mi, BinaryFirstRec(nums, target, lo, mi - 1))


def BinaryFirst(nums: list[int], target: int) -> int:
    lo = 0
    hi = len(nums) - 1
    result = -1

    while lo <= hi:
        mi = lo + (hi - lo) // 2

        if nums[mi] < target:
            lo = mi + 1
        elif nums[mi] == target:
            result = mi
            hi = mi - 1
        else:
            hi = mi - 1

    return result


def BinaryLastRec(nums: list[int], target: int, lo: int, hi: int) -> int:
    if lo > hi:
        return -1

    mi = lo + (hi - lo) // 2

    if nums[mi] < target:
        return BinaryLastRec(nums, target, mi + 1, hi)
    if nums[mi] > target:
        return BinaryLastRec(nums, target, lo, mi - 1)
    return max(mi, BinaryLastRec(nums, target, mi + 1, hi))


def BinaryLast(nums: list[int], target: int) -> int:
    lo = 0
    hi = len(nums) - 1
    result = -1

    while lo <= hi:
        mi = lo + (hi - lo) // 2

        if nums[mi] < target:
            lo = mi + 1
        elif nums[mi] == target:
            result = mi
            lo = mi + 1
        else:
            hi = mi - 1

    return result


def nextGreatestLetter(self, letters: list[str], target: str) -> str:
    N = len(letters)
    lo = 0
    hi = N - 1
    result = -1

    while lo <= hi:
        mi = lo + (hi - lo) // 2

        if letters[mi] < target:
            lo = mi + 1
        elif letters[mi] > target:
            result = mi
            hi = mi - 1
        else:
            lo = mi + 1

    if result == -1:
        return letters[0]

    return letters[result]


if '__main__' == __name__:
    print(BinarySearchRec([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 0, 8))
    print(BinarySearchRec([1, 2, 3, 4, 5, 6, 7, 8, 9], 22, 0, 8))

    print(BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, ))
    print(BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 22, ))

    print(LowerBoundRec([1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 9], 3, 0, 12))
    print(LowerBoundRec([1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 9], 4, 0, 12))

    print(LowerBound([1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 9], 3))
    print(LowerBound([1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 9], 4))

    print(UpperBoundRec([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 0, 8))
    print(UpperBoundRec([1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 0, 8))

    print(UpperBound([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
    print(UpperBound([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))

    print(BinaryFirstRec([1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 9], 3, 0, 12))
    print(BinaryFirstRec([1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 9], 4, 0, 12))

    print(BinaryFirst([1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 9], 3))
    print(BinaryFirst([1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 9], 4))

    print(BinaryLastRec([1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 9], 3, 0, 12))
    print(BinaryLastRec([1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 9], 4, 0, 12))

    print(BinaryLast([1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 9], 3))
    print(BinaryLast([1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 9], 4))
