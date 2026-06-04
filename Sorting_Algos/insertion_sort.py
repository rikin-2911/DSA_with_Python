arr = [7, 3, 5, 2]

for i in range(1, len(arr)):

    current = arr[i]  # i = 0, 1, 2, 3
    j = i - 1

    while (j >= 0) and (arr[j] > current):

        arr[j + 1] = arr[j]

        j -= 1

    arr[j + 1] = current

print(arr)

