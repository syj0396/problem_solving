#문자열을 배열에 저장

N = int(input())

for i in range(N):
    first, second = input().split()
    
    first_l = list(first)
    second_l = list(second)
    
    print("%s & %s are " %(first, second), end='')
    if sorted(first_l) != sorted(second_l):
        print("NOT ", end='')
    print("anagrams.")
    '''
    for c in first_l:
        if c not in second_l:
            break
        else:
            second_l.remove(c)
    
    print("%s & %s are " %(first, second), end='')
    if len(first) != len(second) and len(second_l) != 0:
        print("NOT ", end='')
    print("anagrams.")'''
