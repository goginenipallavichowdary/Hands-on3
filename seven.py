def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_half = array[:middle]
        right_half = array[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        left_index = right_index = merged_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                array[merged_index] = left_half[left_index]
                left_index += 1
            else:
                array[merged_index] = right_half[right_index]
                right_index += 1
            merged_index += 1

        while left_index < len(left_half):
            array[merged_index] = left_half[left_index]
            left_index += 1
            merged_index += 1

        while right_index < len(right_half):
            array[merged_index] = right_half[right_index]
            right_index += 1
            merged_index += 1

sample_array = [5, 2, 4, 7, 1, 3, 2, 6]
print("Original Array:", sample_array)

merge_sort(sample_array)

print("Sorted Array:", sample_array)

def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_half = array[:middle]
        right_half = array[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        left_index = right_index = merged_index = 0
…sample_array = [5, 2, 4, 7, 1, 3, 2, 6]
print("Original Array:", sample_array)

merge_sort(sample_array)

print("Sorted Array:", sample_array)





'''Original Array: [5, 2, 4, 7, 1, 3, 2, 6]
Sorted Array: [1, 2, 2, 3, 4, 5, 6, 7]'''


