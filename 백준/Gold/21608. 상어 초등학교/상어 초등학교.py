n = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

room = [[0] * n for _ in range(n)]
students = []
for _ in range(n**2):
    student = list(map(int, input().split()))
    students.append(student)

for order in range(n**2):
    student = students[order]

    tmp = []

    for i in range(n):
        for j in range(n):
            if room[i][j] == 0:
                like = 0
                empty = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if room[nx][ny] in student[1:]:
                            like += 1
                        if room[nx][ny] == 0:
                            empty += 1
                tmp.append([like, empty, i, j])

    tmp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    room[tmp[0][2]][tmp[0][3]] = student[0]

answer = 0
students.sort()

for i in range(n):
    for j in range(n):
        like = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if room[nx][ny] in students[room[i][j] - 1]:
                    like += 1

        if like != 0:
            answer += 10 ** (like-1)

print(answer)