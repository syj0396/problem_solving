from operator import indexOf


num = int(input())
#list에 input 받고, max 지우고, 두 원소의 합과 비교.
#이는 max와 나머지 두 수를 쉽게 판별하기 위함. 그냥 변수에 받으면 무엇이 max인지 파악하기 힘들다고 생각해서.

for i in range(num):
    inputs = [int(x) for x in input().split()]
    max_v = max(inputs)
    inputs.remove(max_v)
    sum = inputs[0] + inputs[1]

    print("Case #%d: " %(i+1), end="")
    if max_v >= sum:
        print("invalid!")
    else:
        #2개 이상 같으면, 그 중에서 3개가 같으면
        if max_v == inputs[0] or max_v == inputs[1] or inputs[0] == inputs[1]:
            if max_v == inputs[0] and max_v == inputs[1]:
                print("equilateral")
            else:
                print("isosceles")
        else:
            print("scalene")
    