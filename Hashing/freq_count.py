todays_orders = [
    "Biryani", "Dosa", "Biryani", "Burger",
    "Dosa", "Biryani", "Burger", "Dosa", "Biryani"
]


def count_orders(orders):

    freq = {}

    for dish in orders:
        if dish in freq:
            freq[dish] = freq[dish] + 1

        else:
            freq[dish] = 1 
        
    return freq


result = count_orders(todays_orders)
print(result)

# TC -> O(1)
