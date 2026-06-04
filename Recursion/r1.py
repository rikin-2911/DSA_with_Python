def eat_mangoes(count):

    # First check the count = 0 (BASE CASE -> ALWAYS WRITE IT !)
    if count == 0: # 2!= 0
        print("Hand is Empty. Done!")
        return
    
    print(f"I have {count} mangoes. Eating one")

    # Decrement to 0 (RECURSIVE CASE)
    eat_mangoes(count - 1)
    """
    3-1 = 2

    """

eat_mangoes(10)