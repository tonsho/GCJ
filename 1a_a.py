# -*- coding: utf-8 -*-


def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        r, c = raw_input().split(" ")
        rows = []
        for j in xrange(int(r)):
            rows.append(raw_input())
        print "Case #{}\n{}:".format(i, solve(rows))


def solve(rows):
    for y in enumerate(rows):
        for x in y:
            pass


if __name__ == '__main__':
    main()
