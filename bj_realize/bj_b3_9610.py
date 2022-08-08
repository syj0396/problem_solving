q1, q2, q3, q4, axis = 0, 0, 0, 0, 0

num = int(input())
for i in range(num):
    x, y = input().split()
    x = int(x)
    y = int(y)

    if x != 0 and y != 0:
        if x > 0:
            if y > 0:
                q1 += 1
            else:
                q4 += 1
        else:
            if y > 0:
                q2 += 1
            else:
                q3 += 1
    else:
        axis += 1

print("Q1: %d\nQ2: %d\nQ3: %d\nQ4: %d\nAXIS: %d" %(q1, q2, q3, q4, axis))
