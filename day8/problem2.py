from functools import reduce

if __name__ == '__main__':
    with open('day8/input.txt', encoding="utf-8") as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]
    nrows = len(lines)
    ncols = len(lines[0])
    
    max_scenic = 0
    
    for row in range(1, nrows-1):
        for col in range(1,ncols-1):
            height = int(lines[row][col])
            
            distances = []
            
            # Try going in right direction
            i = 1
            while (col + i) < len(lines[0]) - 1:
                if int(lines[row][col + i]) < height:
                    i += 1
                else:
                    break
            distances.append(i)

            # Try going in left direction
            i = 1
            while (col - i) > 0:
                if int(lines[row][col - i]) < height:
                    i += 1
                else:
                    break
            distances.append(i)
            
            # Try going in top direction
            i = 1
            while (row + i) < len(lines) - 1:
                if int(lines[row + i][col]) < height:
                    i += 1
                else:
                    break
            distances.append(i)

            # Try going in bottom direction
            i = 1
            while (row - i) > 0:
                if int(lines[row - i][col]) < height:
                    i += 1
                else:
                    break
            distances.append(i)
            
            scenic_score = reduce(lambda x, y: x * y, distances)
            if max_scenic < scenic_score:
                max_scenic = scenic_score
    
    print("The maximum scenic score is: " + str(max_scenic))