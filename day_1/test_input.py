if __name__ == '__main__':
    with open("input.txt") as f:
        content = [line for line in f.read().strip().split('\n')]
        print(content)
