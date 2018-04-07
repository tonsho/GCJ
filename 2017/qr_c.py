# -*- coding: utf-8 -*-
from math import log


def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, k = raw_input().split(" ")
        print "Case #{}: {} {}".format(i, *solve(int(n), int(k)))


def solve(n, k):
    log_k = int(log(k + 1, 2))
    just_factorial_k = 2 ** log_k - 1
    remain_k = k - just_factorial_k

    empty_width = int((n - just_factorial_k) / (just_factorial_k + 1))

    if remain_k == 0:
        prev_log_k = log_k - 1
        prev_just_factorial_k = 2 ** prev_log_k - 1
        prev_empty_width = int((n - prev_just_factorial_k) / (prev_just_factorial_k + 1))
        if prev_empty_width % 2:
            return empty_width, empty_width
        else:
            return empty_width + 1, empty_width

    rest_nums = (n - just_factorial_k) - (just_factorial_k + 1) * empty_width
    if remain_k <= rest_nums:
        empty_width += 1

    pos = empty_width / 2
    left = pos
    right = empty_width - pos - 1
    return left, right


if __name__ == '__main__':
    main()
