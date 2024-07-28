def pointer_of_blocks(list, n):
    max_value = 0
    counter = 0
    for i in range(n):
        max_value = max(max_value, list[i])
        if i == max_value:
            counter += 1
    return counter


def main():
    with open("input.txt", "r") as file_in:
        line = file_in.readlines()
        n = int(line[0])
        list = [int(x) for x in line[1].split()]
    result = pointer_of_blocks(list, n)
    with open("output.txt", "w") as file_out:
        file_out.write(str(result))
if __name__ == '__main__':
    main()