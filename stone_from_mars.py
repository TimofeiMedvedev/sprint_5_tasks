def counter_stone(stone_from_mars, stone_from_earth):
    list_sum = stone_from_mars + stone_from_earth
    count_mars = [0] * (max(list_sum)+1)
    count_earth = [0] * (max(list_sum)+1)
    for i in stone_from_mars:
        count_mars[i] += 1
    for j in stone_from_earth:
        count_earth[j] += 1
    s_e = 0
    s_m = 0
    for item in range(len(count_mars)):
        s_e += count_earth[item]
        s_m += count_mars[item]
        if s_m > s_e:
            s_m = s_e
        min_s = min(s_e, s_m)
    return min_s


if __name__ == '__main__':
    q_stone_earth = 10
    stone_from_earth = [8, 5, 5, 8, 6, 9, 8, 2, 4, 7]
    q_stone_from_mars = 8
    stone_from_mars = [9, 8, 1, 1, 1, 5, 10, 8]
    # q_stone_earth = 10
    # stone_from_earth = [8, 2, 4, 7, 8, 5, 5, 8, 6, 9]
    # q_stone_from_mars = 13
    # stone_from_mars = [9, 8, 1, 1, 1, 5, 10, 8, 2, 7, 4, 3, 15]
    # q_stone_earth = 8
    # stone_from_earth = [5, 10, 3, 1, 8, 5, 7, 5]
    # q_stone_from_mars = 3
    # stone_from_mars = [4, 4, 3]  
    # q_stone_earth = int(input())
    # stone_from_earth = [int(x) for x in input().split()]
    # q_stone_mars = int(input())
    # stone_from_mars = [int(x) for x in input().split()]

    print(counter_stone(stone_from_mars, stone_from_earth))