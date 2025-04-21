def solution(friends, gifts):
    idx = {f:i for i,f in enumerate(friends)}
    n = len(friends)
    cnt = [[0]*n for _ in range(n)]
    score = [0]*n
    gi = [0]*n
    for gift in gifts:
        a,b = gift.split()
        i,j = idx[a], idx[b]
        cnt[i][j] += 1; 
        gi[i] += 1
        gi[j] -= 1
    for i in range(n):
        for j in range(i+1, n):
            if cnt[i][j] > cnt[j][i]:
                score[i] += 1
            elif cnt[i][j] < cnt[j][i]:
                score[j] += 1
            elif gi[i] > gi[j]:
                score[i] += 1
            elif gi[i] < gi[j]:
                score[j] += 1
    return max(score)
