# Quick Sort Algorithm
This program will take in a list/array and return a sorted version using quick sort algorthim. Both version 1 and version 2 uses the same method, there is no difference between the two. 

## Function 1: quicksort
### Parameters:
unorderedlist: a list of integers to be sorted
left: index of the first element
right: index of the last element

1. The function finds the correct position of the last element by calling the partition function.
2. It then makes two recursive calls to its self:
Recursive call #1: the function will sort a value from the first half of the list.
Recursive call #2: the function will sort a value from the second hald of the list. 
3. The function will continue to sort one element at a time until all the values are sorted.

### Output
This functions doesn't return anything, but will sort the list in place


## Function 2: partition
Function selects the last element as the pivot, and finds the correct position of the pivot, such that all the elements before the pivot are smaller, and all the elements after the pivot are bigger. 

### variables:
pivot: takes the value of the last element.
i: starts at the beginning of the list, taking the index of the first element, and increments until it finds a value greater than the pivot.
j: starts at the end of the list, taking the index of the element before the pivot, and decrement until it finds a value less than the pivot.

### Output
Function will return the index of the position of the pivot element.


## Use cases
```python
print(quicksort_v1([5, 4, 3, 2, 1]))
```
Expected output: [1, 2, 3, 4, 5]

```python
print(quicksort_v1([3, 1]))
```
Expected output: [1, 3]
