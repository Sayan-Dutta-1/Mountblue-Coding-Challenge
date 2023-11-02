def find_unlocking_key(locking_key):
    # Convert the locking key to a list of characters
    locking_key = list(str(locking_key))
    
    # Sort the list in ascending order
    locking_key.sort()
    
    # If the first character is '0', find the first non-zero character and swap it with the first character
    if locking_key[0] == '0':
        for i in range(1, len(locking_key)):
            if locking_key[i] != '0':
                locking_key[0], locking_key[i] = locking_key[i], locking_key[0]
                break
    
    # Convert the list back to a string to get the unlocking key
    unlocking_key = ''.join(locking_key)
    
    return int(unlocking_key)

# Test the function
locking_key = 3802
print("The unlocking key is:", find_unlocking_key(locking_key))
