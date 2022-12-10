class Directory:
    def __init__(self, name, parent_dir):
        self.files_children = []
        self.dir_children = []
        self.name = name
        self.size = 0
        self.parent_dir = parent_dir
    
    def add_children(self, files, dirs):
        if files:
            self.files_children.append(files)
        if dirs:
            self.dir_children.append(dirs)

    def calculate_size(self):
        size_files = sum([file.get_size() for file in self.files_children])
        size_dirs = sum([dir.calculate_size() for dir in self.dir_children])
        self.size = size_files + size_dirs
        return self.size
    
    def return_sub_dir(self, name):
        return [dir for dir in self.dir_children if dir.name == name][0]

class File:
    def __init__(self, name, parent_dir, size):
        self.name = name
        self.size = size
        self.parent_dir = parent_dir
    
    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def get_parent_dir(self):
        return self.parent_dir

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
    total = 0
    curr_dir = root
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
        if size <= 100000:
            total += size
    
    print("The total size of < 100000 size dirs is: " + str(total))