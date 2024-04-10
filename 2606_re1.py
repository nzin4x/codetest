M = int(input())
N = int(input())
edges = [[] for _ in range(M + 1)]
answers = []
for _ in range(N):
    a, b = map(int, input().split())
    edges[a].append(b)


def dfs(n):
    answers.append(n)

    for v in edges[n]:
        if v not in answers:
            dfs(v)

dfs(1)

print(answers)
