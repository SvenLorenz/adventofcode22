if __name__ == '__main__':
    with open('day4/input.txt', encoding="utf-8") as f:
        lines = f.readlines()
    
    counter = 0
    for line in lines:
        first_elve = line.split(",")[0]
        second_elve = line.split(",")[1]
        
        first_elve = [int(i) for i in first_elve.split("-")]
        second_elve = [int(i) for i in second_elve.split("-")]
        
        if (first_elve[0] <= second_elve[0] and first_elve[1] >= second_elve[1]) or (first_elve[0] >= second_elve[0] and first_elve[1] <= second_elve[1]):
            counter += 1
            
    
    print("The counter is: " + str(counter))