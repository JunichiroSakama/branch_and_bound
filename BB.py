#!/usr/bin/python3

## 最大容量
C = 15
## 品物の価格、重さ
S = ((50, 7), (40, 5), (10, 1), (70, 9), (55, 6))
## 価格/重さでソート
tmp = [S[i][0]/S[i][1] for i in range(len(S))]
sorted_S = []
for _ in range(len(tmp)):
    sorted_S.append(S[tmp.index(max(tmp))])
    tmp[tmp.index(max(tmp))] = -1
sorted_S = tuple(sorted_S)
## 解く問題のキュー
Q = []
## 現在解いている問題
current = ()

def ub():
    sum_ = 0
    value = 0
    next_index = -1
    opt = [0 for _ in range(len(sorted_S))]
    if len(current) != 0:
        for i in current:
            if 0 < i:
                opt[i] = 1
                sum_ += sorted_S[i][1]
                value += sorted_S[i][0]
            else:
                opt[-i] = -1
    for i in range(len(sorted_S)):
        if opt[i] == 0:
            if sum_ + sorted_S[i][1] <= C:
                opt[i] = 1
                sum_ += sorted_S[i][1]
                value += sorted_S[i][0]
            else:
                opt[i] = C - sum_
                add =  sorted_S[i][0] / sorted_S[i][1] * opt[i]
                value += add
                next_index = i if add != 0 else -1
                break
    return (value, opt, next_index)


def lb():
    sum_ = 0
    value = 0
    opt = [0 for _ in range(len(sorted_S))]
    if len(current) != 0:
        for i in current:
            if 0 < i:
                opt[i] = 1
                sum_ += sorted_S[i][1]
                value += sorted_S[i][0]
            else:
                opt[-i] = -1
    for i in range(len(sorted_S)):
        if opt[i] == 0 and sum_ + sorted_S[i][1] <= C:
            opt[i] = 1
            sum_ += sorted_S[i][1]
            value += sorted_S[i][0]
    return (value, opt)

## 初期化
LB = lb()
UB = ub()
BEST = LB[0]
OPT = LB[1]
if LB == UB:
    print('{} is best.'.format(BEST))
Q.append(UB[2])
Q.append(-UB[2])
## 初期化ここまで

## 途中経過表示用関数
def print_process():
    print('current : {}'.format(current))
    print('best : {}'.format(BEST))
    print('opt : {}'.format(OPT))
    print('UB : {}'.format(UB))
    print('LB : {}'.format(LB))
    print('Q : {}'.format(Q))
    print('-'*40)
#    print('-'*20+'end init'+'-'*20)

print_process()


## Qがなくなるまで続ける
while Q:
    UB = LB = ''
    if type(Q[0]) == int:
        current = tuple([Q[0]])
    else:
        current = Q[0]
    del(Q[0])
    UB = ub()
    if UB[0] > BEST:
        LB = lb()
        if LB[0] > BEST:
            BEST = LB[0]
            OPT = LB[1]
        if UB[0] > LB[0]:
            Q.append(current + tuple([UB[2]]))
            Q.append(current + tuple([-UB[2]]))
    print_process()


## ソートする前の品物の順番に対応させて答えの出力
def ans():
    global OPT
    tmp = []
    for i in range(len(OPT)):
        if OPT[i] == 1:
            tmp.append(sorted_S[i])
    OPT = [1 if t in tmp else 0 for t in S ]
    print('best : {}'.format(BEST))
    print('opt  : {}'.format(OPT))

ans()
