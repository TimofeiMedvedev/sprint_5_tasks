def array_in_pattern(array, pattern):   
    # pattern = [3, 10, 5, 9, 2, 7, 6, 0]
    # len_pattern = 8
    # array = [3, 10, 5, 9, 2, 7, 6, 0, 8, 3, 4]
    # len_array = 11
    len_pattern = len(pattern)
    count = [0] * (max(array)+1)
    new_list_1 = []
    sorted_list = []
    for item in array:
        count[item] += 1
        if item not in pattern:
            new_list_1 += [item]
    for i in range(len_pattern):
        if pattern[i] in array:
            sorted_list += [pattern[i]] * count[pattern[i]]
    all_list = sorted_list + sorted(new_list_1)
    return all_list

def main():
    with open("input.txt", "r") as file_in:
        line = file_in.readlines()
        array = [int(x) for x in line[1].split()]
        pattern = [int(x) for x in line[3].split()]
    result = array_in_pattern(array, pattern)
    with open("output.txt", "w") as file_out:
        file_out.write(' '.join(str(x) for x in result))
if __name__ == '__main__':
    main()
  







