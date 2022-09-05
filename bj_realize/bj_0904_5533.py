#배열 내에 같은 원소가 있으면 그 인덱스를 뽑아내어 자신과 그 번호의 원소를 0으로.
#그다음 0이 아닌 값은 자동으로 점수로 더해질 것.
#근데 알고리즘이 O(n^2)일텐데.. 더 효율적인 방법은 없을까?
'''
def findSame(arr):
    for i in range(N):
        isSame = False
        for j in range(i+1, N):
            if arr[j] != 0 and arr[i] == arr[j]:
                isSame = True
                arr[j] = 0
        if (isSame):
            arr[i] = 0

N = int(input())

first = [0 for i in range(N)]
second = [0 for i in range(N)]
third = [0 for i in range(N)]
score = [0 for i in range(N)]

for i in range(N):
    first[i], second[i], third[i] = map(int, input().split())

findSame(first)
findSame(second)
findSame(third)

#파이썬에서 배열을 함수로 전달했다가 함수가 끝나면 배열 원소 값이 변형된 채로 유지될까?
for i in range(N):
    print(first[i]+second[i]+third[i])
'''

N = int(input())
arr = [[0 for i in range(N)] for j in range(3)]
score = [0 for i in range(N)]

for i in range(N):
    first, second, third = map(int, input().split())
    arr[0][i] = first
    arr[1][i] = second
    arr[2][i] = third

for i in range(3):
    for j in range(N):
        if arr[i].count(arr[i][j]) == 1:
            score[j] += arr[i][j]

for i in range(N):
    print(score[i])

