"""
Leetcode Question
"""

def dfs(i, nums, subsets, rv):
    if i >= len(nums):
        rv.append(subsets.copy())
        return

    subsets.append(nums[i])
    dfs(i+1, nums, subsets, rv)

    subsets.pop()
    dfs(i+1, nums, subsets, rv)


def main():
    rv = []
    subsets = []
    nums = [1,2,3,4,5]
    dfs(0, nums, subsets, rv)
    print(rv)


if __name__ == '__main__':
    main()
