def find_duplicates(numbers):

    for i in range(len(numbers)):
        for j in range(len(numbers)):

            if i != j and numbers[i] == numbers[j]:
                # ex. 1 != 2 and 1 == 1 -> Truef
                return True
            
    return False

numbers = [10, 35, 22, 48, 22]

result = find_duplicates(numbers)
if result:
    print("Duplicate Found")
else:
    print("Not found")