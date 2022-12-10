from problem1 import File, Directory

if __name__ == '__main__':
    with open('day7/input.txt', encoding="utf-8") as f:
        lines = f.readlines()
        
        root = Directory("/", "")
    curr_dir = root
    
    # create dir structure
    for cmd in lines[1:]:
        cmd = cmd.strip()
        if cmd[0:4] == "$ cd" and not cmd == "$ cd ..":
            sub_dir = cmd.replace("$ cd ", "")
            curr_dir = curr_dir.return_sub_dir(sub_dir)
            continue
        
        if cmd == "$ ls":
            continue
        
        if cmd[0:3] == "dir":
            curr_dir.add_children(None, Directory(cmd.replace("dir ", ""), curr_dir))
            continue
        
        if cmd[0] in ['0','1','2','3','4','5','6','7','8','9']:
            file_info = cmd.split(" ")
            file = File(file_info[1], curr_dir, int(file_info[0]))
            curr_dir.add_children(file, None)
            continue
        
        if cmd == "$ cd ..":
            curr_dir = curr_dir.parent_dir
    
    
    # second loop over to calculate sizes
    curr_dir = root
    needed_space = 30000000 - 70000000 + root.calculate_size()
    possible_removals = []
    for cmd in lines[1:]:
        cmd = cmd.strip()
        if cmd[0:4] == "$ cd" and not cmd == "$ cd ..":
            sub_dir = cmd.replace("$ cd ", "")
            curr_dir = curr_dir.return_sub_dir(sub_dir)
        
        if cmd == "$ ls":
            continue
        
        if cmd[0:3] == "dir":
            continue
        
        if cmd[0] in ['0','1','2','3','4','5','6','7','8','9']:
            continue
        
        if cmd == "$ cd ..":
            curr_dir = curr_dir.parent_dir
            continue
        
        size = curr_dir.calculate_size()
        if size > needed_space:
            possible_removals.append(size)
    
    print("Smallest possible removal is: " + str(min(possible_removals)))