# Most important for Interview and very much asked...

"""
double ended queue

O(1)
"""

from collections import deque

# can add/remove items from both front/back
queue = deque()

queue.append("Arvi")
queue.append("Priya")
queue.append("You")
queue.append("Karan")

print(queue)

first = queue.popleft()
print(first)
print(queue)

print(queue[0])
print(len(queue))

print(len(queue) == 0)
