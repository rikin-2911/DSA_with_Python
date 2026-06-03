import hashlib
hashlib.sha256("ravi@gmail.com".encode()).hexdigest() # For consistent numbers


users = {}

users["ravi@gamil.com"] = "Ravi Sharma"

#key = "ravi@gmail.com"
#value = "Ravi Sharma"
#box = hash(key) % total_boxes 
#store(box, "Ravi Sharma")

print(hash("ravi@gmail.com"))
print(hash("priya@gmail.com"))
print(hash("chirag@gmail.com"))

# Different numbers in every run -> Hash randomization for securing the data in DOS Attack
