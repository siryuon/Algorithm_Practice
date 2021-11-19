def solution(n, computers):
    answer = 0
    visit = [0 for _ in range(n)]
    
    for com in range(n):
        if visit[com] == 0:
            DFS(n, computers, com, visit)
            answer += 1
    
    return answer

def DFS(n, computers, com, visit):
    visit[com] = 1
    
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if visit[connect] == 0:
                DFS(n, computers, connect, visit)
