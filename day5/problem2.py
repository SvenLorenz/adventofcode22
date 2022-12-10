from problem1 import LiFo

if __name__ == '__main__':
    with open('day5/input.txt', encoding="utf-8") as f:
        lines = f.readlines()
        
    stacks_txt = lines[:9]
    instructions = lines[10:]

    stacks = [LiFo(reversed(["W", "L", "S"])),
              LiFo(reversed(["Q", "N", "T", "J"])),
              LiFo(reversed(["J","F","H","C","S"])),
              LiFo(reversed(["B","G","N","W","M","R","T"])),
              LiFo(reversed(["B","Q","H","D","S","L","R","T"])),
              LiFo(reversed(["L","R","H","F","V","B","J","M"])),
              LiFo(reversed(["M","J","N","R","W","D"])),
              LiFo(reversed(["J","D","N","H","F","T","Z","B"])),
              LiFo(reversed(["T","F","B","N","Q","L","H"]))]
    
    instructions = [i.replace("move ", "").replace("from ", "").replace("to ", "") for i in instructions]
    instructions = [[int(j) for j in i.split(" ")] for i in instructions]
    
    for i in instructions:
        from_crate = i[1] - 1
        to_crate = i[2] - 1
        amount = i[0]
        stack_to_be_moved = LiFo([])
        for _ in range(amount):
            stack_to_be_moved.stack_push(stacks[from_crate].get_top())
            stacks[from_crate].stack_pop()
        for _ in range(amount):
            latest_from = stack_to_be_moved.get_top()
            stacks[to_crate].stack_push(latest_from)
            stack_to_be_moved.stack_pop()
            
    top_crates = ""
    for stack in stacks:
        top_crates += stack.get_top()
    print("The top crates are: " + top_crates)