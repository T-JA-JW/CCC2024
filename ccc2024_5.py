from collections import deque

r, c = int(input()), int(input())
arr = [input() for _ in range(r)]
a = int(input())
b = int(input())

dx = [-1, 1, 0, 0] # LRUD
dy = [0, 0, 1, -1] # LRUD
sum = 0
visited = set()
dq = deque()
visited.add((a, b))

if arr[a][b] == 'S':
    sum += 1
elif arr[a][b] == 'M':
    sum += 5
elif arr[a][b] == 'L':
    sum += 10
    
dq.append((a, b))

while dq:
    a, b = dq.popleft()
    for i in range(4):
        nr = a + dx[i]
        nc = b + dy[i]
        # print(nr, nc)
        if nr < 0 or nr >= r or nc < 0 or nc >= c:
            continue
        if arr[nr][nc] == '*':
            continue
        if (nr, nc) in visited:
            continue
        # print(nr, nc)
        visited.add((nr, nc))
        # print(arr[nr][nc])
        if arr[nr][nc] == 'S':
            sum += 1
        elif arr[nr][nc] == 'M':
            sum += 5
        elif arr[nr][nc] == 'L':
            sum += 10
        dq.append((nr, nc))

print(sum)
