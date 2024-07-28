def counter_stone(stone_from_mars, stone_from_earth):
    stone_from_earth_sort = sorted(stone_from_earth)
    stone_from_mars_sort = sorted(stone_from_mars)
    left_idx = 0
    right_idx = 0
    counter = 0
    while left_idx < len(
        stone_from_earth_sort) and right_idx < len(
            stone_from_mars_sort):
        if stone_from_earth_sort[left_idx] <= stone_from_mars_sort[right_idx]:
            counter += 1
            left_idx += 1
        right_idx += 1
    return str(counter)


def main() -> None:
    with open("input.txt", "r") as file_in:
        lines = file_in.readlines()      
        stone_from_earth = [int(x) for x in lines[1].split()]
        stone_from_mars = [int(x) for x in lines[3].split()]
        result = counter_stone(stone_from_mars, stone_from_earth)
    with open("output.txt", "w") as file_out:
        file_out.write(result)

if __name__ == "__main__":
    main()
    