import heapq # Module

hospital = []

heapq.heappush(hospital, (3, "Broken finger"))
heapq.heappush(hospital, (1, "Heart Attack"))
heapq.heappush(hospital, (2, "High fever"))

print(heapq.heappop(hospital))
print(heapq.heappop(hospital))
print(heapq.heappop(hospital))


# Syntax
#heapq.heappush(queue, item_with_priority)
#heapq.heappop(queue)