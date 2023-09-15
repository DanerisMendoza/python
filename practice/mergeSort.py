def merge_sort(arr):
     # Split the input array into two halves
    mid = len(arr) // 2
    #0-5 
    left_half_arr = arr[0:mid]
    #5-10
    right_half_arr = arr[mid:len(arr)]
    print(left_half_arr)
    print(right_half_arr)

    # Recursively sort each half
    left_half_arr = merge_sort(left_half_arr)
    right_half_arr = merge_sort(right_half_arr)

    # Merge the sorted halves
    sorted_arr = []
    left_index, right_index = 0, 0

    while left_index < len(left_half_arr) and right_index < len(right_half_arr):
        if left_half_arr[left_index] < right_half_arr[right_index]:
            sorted_arr.append(left_half_arr[left_index])
            left_index += 1
        else
            sorted_arr.append(right_half_arr[right_index])
            right_index

    sorted_arr.extend(left_half_arr[left_index:])
    sorted_arr.extend(right_half[right_index:])

    return sorted_arr

# arr = [1,2,3,4,5,6,7,8,9,10]
arr = [1,2,3,4,5,6,7,8,9,10]
merge_sort(arr)