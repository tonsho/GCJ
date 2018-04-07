# -*- coding: utf-8 -*-


def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = raw_input()
        print "Case #{}: {}".format(i, solve(n))


def solve(n):
    not_tidy_pos = 0
    for i in xrange(1, len(n)):
        if n[i - 1] <= n[i]:
            continue
        else:
            not_tidy_pos = i
            break
    else:
        return n

    tidy_pos = 1
    for j in range(not_tidy_pos)[:0:-1]:
        if n[j - 1] < (n[j]):
            tidy_pos = j + 1
            break

    left_part = int(n[:tidy_pos]) - 1
    right_part = int('9' * (len(n) - tidy_pos))
    return left_part * 10 ** (len(n) - tidy_pos) + right_part


if __name__ == '__main__':
    main()
