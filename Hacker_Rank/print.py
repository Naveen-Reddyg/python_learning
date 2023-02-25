def summingSeries(n):
    return (n*n) % 10000007


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())

        result = summingSeries(n)
        print(result)

    # for i in range(1, n + 1):
    #     print(i, end=' ')
