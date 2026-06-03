users = [
    "ram@gmail.com",
    "om@gmail.com",
    "do@gmail.com"
    #50 M +
]


def login(email):
    for user in users:
        if user ==  email:
            return "Login Success"
        
    return "Not Found !"

print(login("ra@gmail.com"))


## Worst case -> 50M Comparison -> Too Much Time !!! -> O(n)