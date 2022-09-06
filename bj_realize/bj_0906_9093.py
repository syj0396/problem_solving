N = int(input())
for i in range(N):
    str_arr = [list(s) for s in input().split()]
    for s in str_arr:
        s.reverse()
        print(''.join(s), end=' ')
    print()

