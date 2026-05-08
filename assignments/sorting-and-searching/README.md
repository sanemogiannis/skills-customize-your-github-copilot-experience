# 📘 Assignment: Sorting and Searching Algorithms

## 🎯 Objective

In this assignment, you will implement classic sorting and searching algorithms from scratch using Python loops and conditionals. You will strengthen your problem-solving skills and understand how computers organize and find data.

## 📝 Tasks

### 🛠️	Implement Bubble Sort

#### Description
Write a function that sorts a list of numbers in ascending order using the bubble sort algorithm. Bubble sort works by repeatedly swapping adjacent elements that are out of order.

#### Requirements
Completed program should:

- Define a function `bubble_sort(numbers)` that accepts a list of integers.
- Sort the list in ascending order without using Python's built-in `sort()` or `sorted()`.
- Return the sorted list.
- Print the original and sorted list so the result is visible.

Example:
```
Input:  [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
```


### 🛠️	Implement Linear Search

#### Description
Write a function that searches for a target value in a list by checking each element one by one from the beginning.

#### Requirements
Completed program should:

- Define a function `linear_search(numbers, target)` that accepts a list and a target integer.
- Return the index of the target if found, or `-1` if not found.
- Print a message indicating whether the target was found and at which index.

Example:
```
linear_search([11, 12, 22, 25, 34], 22)  →  Found 22 at index 2
linear_search([11, 12, 22, 25, 34], 99)  →  99 not found
```


### 🛠️	Implement Binary Search

#### Description
Write a function that searches a **sorted** list more efficiently by repeatedly halving the search range. This is faster than linear search for large lists.

#### Requirements
Completed program should:

- Define a function `binary_search(numbers, target)` that accepts a sorted list and a target integer.
- Return the index of the target if found, or `-1` if not found.
- Use a loop (not recursion) to divide the search range each step.
- Print which search method found the target faster when comparing both on the same list.
