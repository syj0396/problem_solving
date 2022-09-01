while True:
    num_list = [int(x) for x in input().split()]
    if num_list[0] == -1 and len(num_list) == 1:
        break

    count = -1
    for i in num_list:
        if i * 2 in num_list:
            count += 1
    print(count)