from problem1 import check_unique

if __name__ == '__main__':
    with open('day6/input.txt', encoding="utf-8") as f:
        lines = f.readlines()[0]
          
    for i in range(0, len(lines)-14):
        curr = lines[i:i+14]
        if check_unique(curr):
            print("The solution is: " + str(i + 14))
            break