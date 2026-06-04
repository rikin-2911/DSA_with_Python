def quick_sort(numbers):

    if len(numbers) <= 1:
        return numbers
    
    pivot = numbers[-1] # Taking the last ele as pivot

    smaller = []
    bigger = []

    for number in numbers[:-1]:

        if number <= pivot:
            smaller.append(number)

        else:
            bigger.append(number)

    return quick_sort(smaller) + [pivot] + quick_sort(bigger)

prices = [850, 200, 520, 100, 430]
result = quick_sort(prices)
print("Final Sorted Array: ", result)