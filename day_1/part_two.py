def count_sum_of_measurements(measurements:list)->int:
    count = 0
    window = sum(measurements[:3])
    new_measurements_list = measurements[1:]
    for i,n in enumerate(new_measurements_list):
        if i+3 == len(measurements):
            return count
        else:
            new_window = sum(new_measurements_list[i:i+3])
            if new_window > window:
                count+=1
            window = new_window


if __name__ == '__main__':
    with open("input.txt") as f:
        content = [int(line) for line in f.read().strip().split('\n')]
        print(count_sum_of_measurements(content))
