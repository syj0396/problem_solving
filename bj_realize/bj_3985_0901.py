L = int(input())
N = int(input())
cake = [0 for i in range(L+1)]

expected_max = 0
expected_n = -1

real_max = 0
real_n = -1

for i in range(1, N+1):
    p, k = map(int, input().split())
    if (k - p + 1) > expected_max:
        expected_max = k - p + 1
        expected_n = i

    real = 0
    for j in range(p, k+1):
        if cake[j] == 0:
            cake[j] = i
            real += 1
    if real > real_max:
        real_max = real
        real_n = i

print(expected_n)
print(real_n)
