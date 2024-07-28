def counter_people(list_people, number_takt):
    if len(list_people) > 1:
        for q in range(0, number_takt - 1):
            list_people.append(list_people[q])
        del list_people[:number_takt]
        counter_people(list_people, number_takt)
    return list_people


def main():
    with open("input.txt", "r") as file_in:
        number_people = int(file_in.readline().rstrip())
        number_takt = int(file_in.readline().rstrip())
    list_people = [i for i in range(1, number_people+1)]
    result = counter_people(list_people, number_takt)
    with open("output.txt", "w") as file_out:
        file_out.write(''.join(map(str, result)))


if __name__ == '__main__':
    main()
    # number_people = 5
    # number_takt = 2
    # number_people = int(input())
    # number_takt = int(input())
    # list_people = [i for i in range(1, number_people+1)]
    # print(*counter_people(list_people, number_takt))
   
