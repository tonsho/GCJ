# -*- coding: utf-8 -*-


def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, k = raw_input().split(" ")
        print "Case #{}: {}".format(i, solve(int(n), int(k)))


def solve(n, k):
    empties = [n]
    left = 0
    right = 0
    for i in xrange(k):
        max_empty = max(empties)
        pos = max_empty / 2
        left = pos
        right = max_empty - pos - 1
        del empties[empties.index(max_empty)]
        empties += [left, right]
    return '{} {}'.format(left, right if 0 <= right else 0)


if __name__ == '__main__':
    main()
