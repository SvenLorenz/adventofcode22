import heapq

if __name__ == '__main__':
    with open('day1/input.txt', encoding="utf-8") as f:
        lines = f.readlines()
    
    curr = 0
    heap = []

    for i in range(len(lines) - 1):
        try:
            curr += int(lines[i])
        except ValueError:
            if len(heap) < 3:
                heapq.heappush(heap, curr)
            else:
                heapq.heappushpop(heap, curr)
            curr = 0

    print("The maximum 3 is: " + str(sum(heap)))