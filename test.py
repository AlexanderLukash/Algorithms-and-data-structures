arr = [5, 3, 8, 8, 4, 1]
arr_2 = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
arr_3 = [170, 45, 75, 90, 802, 24, 2, 66]
arr_4 = [3, 1, 2, 5, 4, 6, 8, 7, 10, 9, 2, -2, 4, 5, 12, 4, 0, 1, 3, 1, 2, 5, 4, 6, 8, 7, 10, 9, 2, -2, 4, 5, 12, 4, 0,
         1, 3, 1, 2, 5, 4, 6, 8, 7, 10, 9, 2, -2, 4, 5, 12, 4, 0, 1, 3, 1, 2, 5, 4, 6, 8, 7, 10, 9, 2, -2, 4, 5, 12, 4,
         0, 1]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def bubble_sort(arr: list) -> list:
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


print(f'Bubble sort: {arr}, {bubble_sort(arr[:])}')


def selection_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(f'Selection sort: {arr}, {selection_sort(arr[:])}')


def insertion_sort(arr: list) -> list:
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


print(f'Insertion sort: {arr}, {insertion_sort(arr[:])}')


def quickSort(arr: list, lo: int, hi: int) -> list:
    if lo < hi:
        pi = partition(arr, lo, hi)

        quickSort(arr, lo, pi - 1)
        quickSort(arr, pi + 1, hi)
    return arr


def partition(arr: list, lo: int, hi: int) -> int:
    pivot = arr[hi]
    i = lo - 1

    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


print(f'Quick sort: {arr}, {quickSort(arr[:], 0, (len(arr) - 1))}')


def head_sort(arr: list) -> list:
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def heapify(arr: list, n: int, i: int):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


print(f'Heap sort: {arr}, {head_sort(arr[:])}')


def merge_sort_simple(arr: list) -> list:
    n = len(arr)
    if n > 1:
        ll = arr[:n // 2]
        rl = arr[n // 2:]

        merge_sort_simple(ll)
        merge_sort_simple(rl)

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


print(f'Merge sort simple: {arr}, {merge_sort_simple(arr[:])}')


def merge_sort(arr: list, l: int, r: int) -> list:
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)

    return arr


def merge(arr: list, left: int, mid: int, right: int):
    ll = arr[left:mid + 1]
    rl = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

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


print(f'Merge sort: {arr}, {merge_sort(arr[:], 0, (len(arr) - 1))}')


def shell_sort(arr: list) -> list:
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j - gap] > arr[j]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap //= 2

    return arr


print(f'Shell sort: {arr}, {shell_sort(arr[:])}')


def bucket_sort(arr: list) -> list:
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    i = 0
    for bucket in buckets:
        for num in bucket:
            arr[i] = num
            i += 1

    return arr


print(f'Bucket sort: {arr_2}, {bucket_sort(arr_2[:])}')


def counting_sort(arr: list) -> list:
    n = len(arr)
    max_value = max(arr)
    output = [0] * n
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    for i in range(n):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output


print(f'Counting sort: {arr}, {counting_sort(arr[:])}')


def radix_sort(arr: list) -> list:
    max_value = max(arr)
    n = len(arr)
    exp = 1

    while max_value // exp >= 1:
        for i in range(n - 1):
            counting_sort_exp(arr, exp)
            exp *= 10

    return arr


def counting_sort_exp(arr: list, exp: int) -> list:
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


print(f'Radix sort: {arr_3}, {radix_sort(arr_3[:])}')


def tim_sort(arr: list) -> list:
    n = len(arr)
    min_run = calculate_min_run(n)

    for start in range(0, n, min_run):
        end = min(start + min_run, n - 1)
        insertion_sort_tim(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + size * 2 - 1, n - 1)

            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

    return arr


def calculate_min_run(n):
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort_tim(arr: list, left: int, right: int):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


print(f'Tim sort: {arr_4}, {tim_sort(arr_4[:])}')


def binary_search(arr: list, target: int) -> int:
    n = len(arr)
    lo = 0
    hi = n - 1

    while lo <= hi:
        mi = lo + (hi - lo) // 2
        if arr[mi] == target:
            return mi
        elif arr[mi] < target:
            lo = mi + 1
        else:
            hi = mi - 1
    return -1



print(f'Binary search: {[1, 2, 3, 4, 5, 6, 7, 8, 9]}, 3 : {binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)} ')
