from math import sqrt

if __name__ == '__main__':
    with open('day9/input.txt', encoding="utf-8") as f:
        lines = f.readlines()
        
        
    visited_cells = [[0,0]]
    head = [0,0]
    tail = [0,0]
    for line in lines:
        cmd = line.split(" ")
        
        if cmd[0] == "R":
            head[0] += int(cmd[1])
        elif cmd[0] == "L":
            head[0] -= int(cmd[1])
        elif cmd[0] == "U":
            head[1] += int(cmd[1])
        elif cmd[0] == "D":
            head[1] -= int(cmd[1])
    	
        rel_pos = [h - t for h, t in zip(head, tail)]
        while sqrt(rel_pos[0]**2 + rel_pos[1]**2) > 1.5:
            # move tail one
            to_move = [1 if pos > 0 else -1 if pos < 0 else 0 for pos in rel_pos]
            rel_pos = [old - step for old, step in zip(rel_pos, to_move)]
            tail = [old + step for old, step in zip(tail, to_move)]
            break_flag = False
            for already_vis in visited_cells:
                if tail[0] == already_vis[0] and tail[1] == already_vis[1]:
                    break_flag = True
            if not break_flag:
                visited_cells.append(tail)
    print(visited_cells)
    print("The number of visited cells is: " + str(len(visited_cells)))