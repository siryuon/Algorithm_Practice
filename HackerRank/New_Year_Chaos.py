def minimumBribes(q):
    cnt = 0
    same = 0
    for i in range(len(q)):
        print(i, q[i])
        if i < q[i] - 3:
            return 'Too chaotic'
        cnt += abs(q[i] - i)
        if q[i] == i:
            same += 1
    return cnt - (len(q) - same)

q = [1,2,5,3,7,8,6,4]

print(minimumBribes(q))
