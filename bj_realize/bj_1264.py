

# vowel = ['a', 'e', 'i', 'o', 'u']
vowel = 'aeiou'
while True:
    cnt = 0
    str = input().lower()
    if str[0] == '#':
        break
    for c in str:
        if c in vowel:
            cnt += 1
    print(cnt)