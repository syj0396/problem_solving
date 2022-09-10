# M - i == 8인 i까지. (0부터)
# N - j == 8인 j까지. (0부터)

#어쨌든 잘 칠해져있는지 확인하려면 2차원배열의 모든 원소를 순회하며 확인해야 하므로
#O(n^2) 말고는 생각이 안 나는데.....
#일단 O(n^2)으로 해결한다 하면, 각 블록을 함수에 보내서 그 블록과 맞닿아 있는 부분 검사?

#근데 어차피 정답은 WBWBWB.. 아님 BWBWBW이므로 
N, M = map(int, input().split())
board = [list(input()) for x in range(N)]

N_margin = N - 8
M_margin = M - 8

min_error = M*N
error_list = []

for sr in range(N_margin+1):
    for sc in range(M_margin+1):
        #중첩 for문을 돌리면 체스판 한번 순회하는 것.
        cnt1 = 0
        cnt2 = 0
        for i in range(sr, sr+8):
            for j in range(sc, sc+8):
                if (i+j)%2 == 0:
                    if board[i][j] != 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if board[i][j] != 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        error_list.append(min(cnt1, cnt2))
print(min(error_list))
