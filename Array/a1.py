marks = [80, 73, 74, 93, 75]


# slicing
print(marks[1:4])
print(marks[::2])

"""# remove at last O(1)
marks.pop() 
marks.pop(1) # remove 73 by index
marks.remove(80) # remove 80 by value
print(marks)

# insert at end O(1)
marks.append(199)
print(marks)

# At specific pos O(n)
marks.insert(2, 55)
print(marks)

# access O(1)
print(marks[0])
print(marks[-1])
"""