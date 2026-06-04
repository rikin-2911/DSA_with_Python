signups = [
    "ravi@gmail.com",
    "priya@gmail.com",
    "ravi@gmail.com",
    "sneha@gamil.com",
    "priya@gmail.com",
    "karan@gmail.com",
    "ravi@gmail.com",
]

def remove_dup(emails):

    seen = set() # O(1)

    unique = []  # if this is used O(nf)

    for email in emails:
        if email not in seen:  # O(1)

            unique.append(email)
            seen.add(email) # for skipping in when email repeated
    return unique

clean = remove_dup(signups)
print(clean)