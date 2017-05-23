# -*- coding: utf-8 -*-
from math import pi


def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, k = raw_input_as_ints()
        cakes = []
        for j in xrange(n):
            cakes.append(raw_input_as_ints())
        print "Case #{}: {:.6f}".format(i, solve(k, cakes))


def raw_input_as_ints():
    return [int(x) for x in raw_input().split(" ")]



def solve(k, cakes):
    surfaces = []
    max_side_n_top = {'side': 0.0, 'top': 0.0}
    for i, (r, h) in enumerate(cakes):
        side = 2 * r * h
        top = (r ** 2)
        s = {'r':r, 'side': side, 'top': top}
        surfaces.append(s)
        if max_side_n_top['side'] + max_side_n_top['top'] < side + top:
            max_side_n_top = s

    surfaces_ordered_by_side = sorted(surfaces, reverse=True, key=lambda x:x['side'])
    max_top_in_k = {'top': 0.0}
    stacked_sides = 0.0
    stacked_r = 0
    for s in surfaces_ordered_by_side[:k]:
        stacked_sides += s['side']
        if max_top_in_k['top'] < s['top']:
            max_top_in_k = s

    if max_side_n_top is max_top_in_k:
        return (stacked_sides + max_side_n_top['top']) * pi
    else:
        stacked_sides += (max_side_n_top['side'] - surfaces_ordered_by_side[k]['side'])
        return (stacked_sides + max_side_n_top['top']) * pi



if __name__ == '__main__':
    main()
