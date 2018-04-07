# -*- coding: utf-8 -*-


def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        s, k = raw_input().split(" ")
        print "Case #{}: {}".format(i, solve(s, int(k)))


def solve(s, k):
    bins = ['+' == x for x in s]
    count = 0
    for i in xrange(len(s)):
        if True != bins[i]:
            if (i + k) > len(s):
                return 'IMPOSSIBLE'
            count += 1
            for j in xrange(k):
                bins[i + j] = not bins[i + j]
    return count


if __name__ == '__main__':
    main()
