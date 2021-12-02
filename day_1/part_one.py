import sys


def count_increases(measurements:list)->int:
    count = 0
    for index in enumerate(measurements):
        if index+1 == len(measurements):
            return count
        elif measurements[index+1]>measurements[i]:
            count += 1



if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
        content = [int(line) for line in f.read().strip().split('\n')]
        solution = count_increases(content)
        out.write(str(solution))
