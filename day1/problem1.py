if __name__ == '__main__':
    with open('day1/input.txt', encoding="utf-8") as f:
        lines = f.readlines()

    curr = 0
    max_val = 0

    for i in lines:
        if curr > max_val:
            max_val = curr
        if len(i) == 1:
            curr = 0
        else:
            curr += int(i)

    print("The maximum is: " + str(max_val))

