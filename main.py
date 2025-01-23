ef quick_sort(arr):
    # Base case: An array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot element
    pivot = arr[len(arr) // 2]
    
    # Partition the array into three parts
    left = [x for x in arr if x < pivot]   # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]   # Elements greater than the pivot
    
    # Recursively sort the left and right partitions, and combine
    return quick_sort(left) + middle + quick_sort(right)
    print(quicksort([3,6,8,10,1,2,1]))  # Output: [1, 1, 2, 3, 6, 8, 10]