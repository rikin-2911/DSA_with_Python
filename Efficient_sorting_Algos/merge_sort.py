def merge_sort(numbers):

    if len(numbers) <= 1:
        return numbers
    
    middle = len(numbers) // 2

    left_half = numbers[:middle] # numbers[:2]
    right_half = numbers[middle:] # numbers[2:]

    print(f"Splitting: {numbers}")
    print(f"Left Half: {left_half}")
    print(f"Right Half: {right_half}")

    sorted_left = merge_sort(left_half)  #[850, 200]
    sorted_right = merge_sort(right_half) # [520, 100, 430]

    sorted_result = combine(sorted_left, sorted_right)

    print(f"Merged Back: {sorted_result}")

    return sorted_result

def combine(left, right):
    final_list = []
    left_pointer = 0
    right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):

        left_item = left[left_pointer]
        right_item = right[right_pointer]

        if left_item <= right_item:
            final_list.append(left_item)
            left_pointer = left_pointer + 1
        else:
            final_list.append(right_item)
            right_pointer = right_pointer + 1

    remaining_left = left[left_pointer:]
    remaining_right = right[right_pointer:]

    final_list = final_list + remaining_left + remaining_right

    return final_list


# Test Cases.....
prices = [850, 200, 520, 100, 430]
result = merge_sort(prices)
print(result)