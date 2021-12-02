import sys


def count_increases(measurements:list)->int:
    count = 0
    for i,_ in enumerate(measurements):
        if i+1 == len(measurements):
            return count
        elif measurements[i+1]>measurements[i]:
            count += 1



if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
        content = [int(line) for line in f.read().strip().split('\n')]
        solution = count_increases(content)
        out.write(str(solution))
