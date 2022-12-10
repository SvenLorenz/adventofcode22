if __name__ == '__main__':
    with open('day4/input.txt', encoding="utf-8") as f:
        lines = f.readlines()
    
    counter = 0
    for line in lines:
        first_elve = line.split(",")[0]
        second_elve = line.split(",")[1]
        
        first_elve = [i for i in range(int(first_elve.split("-")[0]), int(first_elve.split("-")[1]) + 1)]
        second_elve = [i for i in range(int(second_elve.split("-")[0]), int(second_elve.split("-")[1]) + 1)]
        
        if any([i in second_elve for i in first_elve]):
            counter += 1
            
    
    print("The counter is: " + str(counter))