def isOk(row, col):
    if row < 0 or col > 7:
        return False
    else:
        return True

row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
col = [1, 2, 3, 4, 5, 6, 7, 8]
moves = {'R': [0, 1], 'L': [0, -1], 'T': [1, 0], 'B': [0, -1],
        'RT': [1, 1], 'LT': [1, -1], 'RB': [-1, 1], 'LB': [-1, -1]}

K, S, N = input().split()
K_loc = list(K)
S_loc = list(S)
K_r = row.index(K_loc[0])
K_c = col.index(int(K_loc[1]))
S_r = row.index(S_loc[0])
S_c = col.index(int(S_loc[1]))

for i in range(int(N)):
    mv = input()
    #임시에 저장했다가, 인덱스 조건에 만족하고, 돌 위치와 같을경우 돌 이동했을 때 돌도 인덱스 조건에 부합할 때 최종 이동.
    t_r = K_r + moves[mv][1]
    t_c = K_c + moves[mv][0]
    if not isOk(t_r, t_c):
        continue

    if t_r == S_r and t_c == S_c:
        st_r = S_r + moves[mv][1]
        st_c = S_c + moves[mv][0]
        if not isOk(st_r, st_c):
            continue
        S_r = st_r
        S_c = st_c
    
    K_r = t_r
    K_c = t_c

print("%c%d" %(row[K_r], col[K_c]))
print("%c%d" %(row[S_r], col[S_c]))