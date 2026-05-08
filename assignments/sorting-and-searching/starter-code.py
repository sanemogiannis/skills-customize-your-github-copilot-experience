# Sorting and Searching Algorithms
# Implement each function below and test it with the provided examples.


def bubble_sort(numbers):
    """Sort a list of numbers in ascending order using bubble sort.
    
    Args:
        numbers: A list of integers to sort.

    Returns:
        The sorted list.
    """
    # TODO: Implement bubble sort
    # Hint: Use nested loops. In each pass, compare adjacent elements
    # and swap them if they are in the wrong order.
    pass


def linear_search(numbers, target):
    """Search for a target value by checking each element one by one.

    Args:
        numbers: A list of integers to search.
        target: The integer to find.

    Returns:
        The index of target if found, otherwise -1.
    """
    # TODO: Implement linear search
    # Hint: Loop through the list and compare each element to target.
    pass


def binary_search(numbers, target):
    """Search for a target value in a sorted list using binary search.

    Args:
        numbers: A sorted list of integers.
        target: The integer to find.

    Returns:
        The index of target if found, otherwise -1.
    """
    # TODO: Implement binary search
    # Hint: Keep track of low and high boundaries.
    # Check the middle element each time and narrow the range.
    pass


# --- Test your functions below ---

sample = [64, 34, 25, 12, 22, 11, 90]
print("Original:", sample)

sorted_list = bubble_sort(sample.copy())
print("Sorted:  ", sorted_list)

target = 22
idx = linear_search(sorted_list, target)
print(f"Linear search for {target}: index {idx}")

idx = binary_search(sorted_list, target)
print(f"Binary search for {target}: index {idx}")
