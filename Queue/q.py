queue = []

#enqueue
queue.append("Ravi")
queue.append("Priya")
queue.append("You")

print(queue)

# dequeue -> O(n)
first = queue.pop(0)
print(first)
print(queue)