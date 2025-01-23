def merge_sort(arr):
    # Base case: An array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    merged = []
    i = j = 0

    # Merge the two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements from the left and right arrays
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

print merge_sort([38, 27, 43, 3, 9, 82, 10])  # Output: [3, 9, 10, 27, 38, 43, 82]
