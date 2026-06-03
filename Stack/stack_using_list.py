stack = []


stack.append("a")
stack.append("b")
stack.append("c") # Top or last item in stack


print(stack)

print("Top Item", stack[-1])

item = stack.pop()
print("Popped Item: ", item)
print(stack)

print(len(stack) == False)