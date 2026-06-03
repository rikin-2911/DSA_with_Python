users = {}

# All ops are Always done on Key 
# Insert
users["ravi@gmail.com"] = "Ravi Sharma"
users["priya@gmail.com"] = "Priya Patil"
users["chirag@gmail.com"] = "Chirag patel"

print(users)
print(users["ravi@gmail.com"]) # With O(1)

print("ravi@gmail.com" in users) # checking in dict


users["priya@gmail.com"] = "Priya Sharma" # Update using key

del users["chirag@gmail.com"] # delete user using key

print(users.keys())
print(users.values())