# -*- coding: utf-8 -*-


def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        d, n = raw_input_as_ints()
        houses = []
        for i_n in xrange(n):
            houses.append(raw_input_as_ints())
        print "Case #{}: {:.6f}".format(i, solve(d, houses))


def raw_input_as_ints():
    return [int(x) for x in raw_input().split(" ")]


def solve(d, houses):
    times = [float(d - k) / s for k, s in houses]
    t_max = max(times)
    return d / t_max

if __name__ == '__main__':
    main()
