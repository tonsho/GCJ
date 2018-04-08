# -*- coding: utf-8 -*-
def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        _ = input()
        nums = [int(x) for x in input().split(' ')]
        ans = solve(nums)
        print("Case #{}: {}".format(i, ans))


def solve(nums):
    # trouble sort
    ts_nums = nums[::]
    while True:
        changed = False
        for i in range(len(nums) - 2):
            if ts_nums[i + 2] < ts_nums[i]:
                _ = ts_nums[i]
                ts_nums[i] = ts_nums[i + 2]
                ts_nums[i + 2] = _
                changed = True
        if not changed:
            break

    # correct sort
    nums.sort()

    for i, (x, y) in enumerate(zip(nums, ts_nums)):
        if x != y:
            return i

    return 'OK'


if __name__ == '__main__':
    main()
