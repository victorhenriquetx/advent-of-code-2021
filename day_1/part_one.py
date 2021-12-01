def count_increases(measurements:list)->int:
    count = 0
    for i,_ in enumerate(measurements):
        if i+1 == len(measurements):
            return count
        elif measurements[i+1]>measurements[i]:
            count += 1



if __name__ == '__main__':
    with open("input.txt") as f:
        content = [int(line) for line in f.read().strip().split('\n')]
        print(count_increases(content))
