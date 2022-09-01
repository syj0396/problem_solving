#오른쪽: (n+1)%6, 왼쪽: (n-1)%6 -> 이렇게 할 경우 6번 돼지는 0번째 인덱스
#맞은편: (n+3)%6
#배열을 두 개 만들면 되겠지만, 하나만 만들어서 해결하는 방법은 없을까?
#그런데 어차피 한 돼지의 식사량은 3번 참조되니까 3번씩 더하면 되지 않나?

num = int(input())
for i in range(num):
    N = int(input())
    food_list = [int(x) for x in input().split()]
    day = 1
    food_sum = sum(food_list)
    while (food_sum <= N):
        food_sum *= 4
        day += 1
    print(day)

