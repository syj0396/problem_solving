num = int(input())
gan = [1, 2, 3, 3, 4, 10]
sa = [1, 2, 2, 2, 3, 5, 10]

for i in range(num):
    one = [int(a) for a in input().split()]
    two = [int(b) for b in input().split()]
    
    gan_score = []
    two_score = []

    for score, num in zip(gan, one):
        gan_score.append(score*num)
    
    for score, num in zip(sa, two):
        two_score.append(score*num)

    gan_score = sum(gan_score)
    two_score = sum(two_score)

    if gan_score > two_score:
        print("Battle %d: Good triumphs over Evil" % (i+1))
    elif gan_score < two_score:
        print("Battle %d: Evil eradicates all trace of Good" % (i+1))
    else:
        print("Battle %d: No victor on this battle field" % (i+1))
    