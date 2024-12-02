from typing import List, Optional


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Perform a binary search on a sorted list to find the index of the target element.

    Args:
        arr (List[int]): A sorted list of integers.
        target (int): The element to search for.

    Returns:
        Optional[int]: The index of the target element if found, otherwise None.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)  # Calculate the middle index
        guess = arr[mid]  # Element at the middle index

        # If the element is found, return its index
        if guess == target:
            return mid

        # If the guessed element is greater than the target, search the left half
        if guess > target:
            high = mid - 1
        else:
            # Otherwise, search the right half
            low = mid + 1

    # Return None if the element is not found
    return None


# Generate a list of numbers from 1 to 100
my_list = [n for n in range(1, 101)]

if __name__ == '__main__':
    # Prompt the user to enter a number to search for
    item = int(input("Enter the number to search: "))

    # Perform binary search
    result = binary_search(my_list, item)

    # Print the result
    if result is None:
        print(f"{item} is not found in the list.")
    else:
        print(f"{item} found at index {result}.")
