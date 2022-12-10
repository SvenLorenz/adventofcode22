def check_unique(string):
 
    # Initialize occurrences of all characters
    char_set = [False] * 128
 
    # For every character, check if it exists
    # in char_set
    for i in range(0, len(string)):
 
        # Find ASCII value and check if it
        # exists in set.
        val = ord(string[i])
        if char_set[val]:
            return False
 
        char_set[val] = True
 
    return True

if __name__ == '__main__':
    with open('day6/input.txt', encoding="utf-8") as f:
        lines = f.readlines()[0]
          
    for i in range(0, len(lines)-4):
        curr = lines[i:i+4]
        if check_unique(curr):
            print("The solution is: " + str(i + 4))
            break