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
        print "Case #{}:".format(i)
        solve(rows)


def solve(rows):
    rows = [[c for c in row] for row in rows]
    last_row_with_initials = None
    for y in xrange(len(rows)):
        last_initial = None
        for x in xrange(len(rows[y])):
            if rows[y][x] != '?':
                if last_initial is None:
                    for x2 in xrange(x):
                        rows[y][x2] = rows[y][x]
                last_initial = rows[y][x]
            elif last_initial:
                rows[y][x] = last_initial

        if last_initial:
            if last_row_with_initials is None:
                for y2 in xrange(y):
                    rows[y2] = rows[y]
            last_row_with_initials = rows[y]
        elif last_row_with_initials:
            rows[y] = last_row_with_initials

    for row in rows:
        print ''.join(row)


if __name__ == '__main__':
    main()
