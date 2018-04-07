# -*- coding: utf-8 -*-
import math


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        d, instructions = input().split(" ")
        ans = solve(int(d), instructions)
        print("Case #{}: {}".format(i, ans))


def solve(d, instructions):
    if d < instructions.count('S'):
        return 'IMPOSSIBLE'

    strength = 1
    damage = 0
    c_pos_list = []
    for pos, i in enumerate(instructions):
        if i == 'C':
            strength *= 2
            c_pos_list.append(pos)
        else:
            damage += strength

    remain = damage - d
    total_move_count = 0
    for c_idx in range(len(c_pos_list) - 1, 0 - 1, -1):
        if remain <= 0:
            break

        right_margin = len(instructions) - (len(c_pos_list) - c_idx) - c_pos_list[c_idx]
        dec = 2 ** c_idx
        move_count = min(math.ceil(remain / float(dec)), right_margin)
        remain -= dec * move_count
        total_move_count += move_count

    return total_move_count


if __name__ == '__main__':
    main()
