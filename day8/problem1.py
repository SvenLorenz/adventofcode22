if __name__ == '__main__':
    with open('day8/input.txt', encoding="utf-8") as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines]
    nrows = len(lines)
    ncols = len(lines[0])
    picked_trees = [[1 if i == 0 or i == (nrows - 1) or j == 0 or j == (ncols - 1) else 0 for i in range(0, nrows)] for j in range(0, ncols)]
    row_curr_left = [int(line[0]) for line in lines]
    row_curr_right = [int(line[ncols-1]) for line in lines]
    col_curr_top = [int(i) for i in [*lines[0]]]
    col_curr_bottom = [int(i) for i in [*lines[nrows-1]]]
    
    # Check rows from left
    for j in range(1, nrows):
        i = 1
        while not row_curr_left[j] == 9 and i < 99:
            if int(lines[j][i]) > row_curr_left[j]:
                if picked_trees[j][i] == 0:
                    picked_trees[j][i] = 1
                row_curr_left[j] = int(lines[j][i])
            i += 1

    # Check rows from right
    for j in range(1, nrows):
        i = ncols - 1
        while not row_curr_right[j] == 9 and i >= 0:
            if int(lines[j][i]) > row_curr_right[j]:
                if picked_trees[j][i] == 0:
                    picked_trees[j][i] = 1
                row_curr_right[j] = int(lines[j][i])
            i -= 1
    
    # Check columns from top
    for j in range(1, ncols):
        i = 1
        while not col_curr_top[j] == 9 and i < 99:
            if int(lines[i][j]) > col_curr_top[j]:
                if picked_trees[i][j] == 0:
                    picked_trees[i][j] = 1
                col_curr_top[j] = int(lines[i][j])
            i += 1
    
    # Check columns from bottom
    for j in range(1, ncols):
        i = nrows - 1
        while not col_curr_bottom[j] == 9 and i >= 0:
            if int(lines[i][j]) > col_curr_bottom[j]:
                if picked_trees[i][j] == 0:
                    picked_trees[i][j] = 1
                col_curr_bottom[j] = int(lines[i][j])
            i -= 1
            
    print("The amount of visible trees are: " + str(sum([sum(tree_line) for tree_line in picked_trees])))