while True:
    num = input()
    if num == "0":
        break
    width = len(num)+1
    for c in num:
        if c == "1":
            width += 2
        elif c == "0":
            width += 4
        else:
            width += 3

    print(width)