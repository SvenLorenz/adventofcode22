if __name__ == '__main__':
    with open('day2/input.txt', encoding="utf-8") as f:
        lines = f.readlines()
    
    score = 0
    
    for line in lines:
        line = line.split("\n")[0].split(" ")
        if line[1] == "X":
            score += 1
            if line[0] == "A":
                score += 3
            elif line[0] == "C":
                score += 6
        elif line[1] == "Y":
            score += 2
            if line[0] == "A":
                score += 6
            elif line[0] == "B":
                score += 3
        elif line[1] == "Z":
            score += 3
            if line[0] == "C":
                score += 3
            elif line[0] == "B":
                score += 6
    
    print("The score is: " + str(score))