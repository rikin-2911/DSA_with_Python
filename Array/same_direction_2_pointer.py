def clean(names):

    left = 0
    
    for right in range(1, len(names)):
        if names[right] != names[left]:
            left = left + 1  # Left Jumps
            names[left] = names[right] # Copy names

    return left + 1

names = ["Aman", "Aman", " Bhavna", "Chirag", "Chirag", "Diya", "Pavan"]

count = clean(names)

print(names[:count])


"""
O(n) -> Time
O(1) -> Space

Same Name -> Right move, left stays. Register does not change
Different -> Left forwardm new name copy left new spot

Asked in Microsoft, Amazon, etc for freshers...
"""