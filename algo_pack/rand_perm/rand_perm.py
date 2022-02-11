import random

def rand(k):
    """returns a random number between 1 and k inclusive.
    """
    return random.randint(1, k)

def shuffle(arr):
    """shuffle an array such that O(N), using swaps and 
    each permutation of the array  has the same probability.
    """
    n = len(arr)
    for i in range(n):
        ip = n - rand(n - i) 
        arr[i], arr[ip] = arr[ip], arr[i]
    return arr


def main()
    """main"""
    dct = dict()
    ITER = 1_000_000
    for i in range(ITER):
        a = ['a','b','c']
        r = tuple(shuffle(a))
        if r in dct:
            dct[r] += 1
        else:
            dct[r] = 1

    for i in dct:
        print(i, dct[i]/ITER)


if __name__ == '__main__':
    main()
