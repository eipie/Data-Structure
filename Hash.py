# Hash 

# 1. Direct Address Tables
    # An array that represents the dynamic set of a universe of elements
    # Each element(slot) corresponds to a key in the universe
    # The table can perform three functions: search, insert and delete 

# 2. Hash Table 
    # Capable of storing large amount of data
    # Uses a hash function h(k) to computer the slot from the key
    # the average-case performance of hasing depends on how well the hash function h 
    # distributes the set of keys to be stored among the m slots
    
# 3. Collision
    # When two keys hash to the same slot, the situation is called a collions
    # A "random"-looking hash function can minimize the number of collions
# 4. Collision resolution by chaining
    # In chaining, we place all the elements that has to the same slot into the same
    # linked list
    # 