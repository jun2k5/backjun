# DFS와 BFS
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	326510	130636	77106	38.546%
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.


from collections import deque

# 입력 처리
n, m, v = map(int, input().split())

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 인접 리스트 정렬 (작은 번호 우선)
for node in graph:
    node.sort()

# DFS (스택 사용)
def dfs():
    visited = [False] * (n + 1)
    stack = [v]
    result = []
    
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            result.append(str(current))
            # 역순으로 스택에 추가하여 작은 번호 먼저 처리
            for neighbor in reversed(graph[current]):
                if not visited[neighbor]:
                    stack.append(neighbor)
    return result

# BFS (큐 사용)
def bfs():
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    result = []
    
    while queue:
        current = queue.popleft()
        result.append(str(current))
        # 정렬된 순서대로 처리
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return result

# 결과 출력
print(' '.join(dfs()))
print(' '.join(bfs()))





# 코드 분석 필수
"""
20250407 공부한 내용 적기


"""

