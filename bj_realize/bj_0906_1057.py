#n번인 사람은 다음 라운드에서 - 홀수이면 +1 -- 2로 나눈 몫이 번호가 됨.
#예를 들어 5번은 다음 라운드에서 (5+1)//2 = 3번.
#김지민과 임한수 번호 중 작은쪽이 홀수이면서 작은쪽에 +1 한게 큰쪽이면 그 라운드에서 대결하는 것.

N, K, L = map(int, input().split())
minimum = min(K, L)
maximum = max(K, L)
round = 1
while True:
    if  minimum % 2 != 0 and minimum + 1 == maximum:
        break
    if minimum % 2 != 0:
        minimum += 1
    if maximum % 2 != 0:
        maximum += 1
    minimum //= 2
    maximum //= 2
    round += 1

print(round)