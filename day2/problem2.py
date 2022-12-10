if __name__ == '__main__':
    with open('day2/input.txt', encoding="utf-8") as f:
        lines = f.readlines()
    
    score = 0
    
    for line in lines:
        line = line.split("\n")[0].split(" ")
        if line[1] == "X":
            if line[0] == "A":
                score += 3
            elif line[0] == "B":
                score += 1
            elif line[0] == "C":
                score += 2
        elif line[1] == "Y":
            score += 3
            if line[0] == "A":
                score += 1
            elif line[0] == "B":
                score += 2
            elif line[0] == "C":
                score += 3
        elif line[1] == "Z":
            score += 6
            if line[0] == "A":
                score += 2
            elif line[0] == "B":
                score += 3
            elif line[0] == "C":
                score += 1
    
    print("The score is: " + str(score))