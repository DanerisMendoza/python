def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the input array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    sorted_arr = []
    left_index, right_index = 0, 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_arr.append(left_half[left_index])
            left_index += 1
        else:
            sorted_arr.append(right_half[right_index])
            right_index += 1

    sorted_arr.extend(left_half[left_index:])
    sorted_arr.extend(right_half[right_index:])
    
    return sorted_arr

# Test the merge_sort function
input_list = [4, 1, 13, 8, 9, 6, 5, 7, 11, 3, 12, 2, 14, 15, 10]
sorted_list = merge_sort(input_list)
print(sorted_list)
