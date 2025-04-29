from collections import deque

def bfs(adj, start):
    V = len(adj)
    res = []
    s = start  # start from user-given node

    q = deque()
    visited = [False] * V
    visited[s] = True
    q.append(s)

    while q:
        curr = q.popleft()
        res.append(curr)

        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return res

if __name__ == "__main__":
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    adj = [[] for j in range(V)]
    print("Enter edges (u v):")
    for j in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)  # because undirected graph

    start_node = int(input("Enter the starting node for BFS: "))

    print("\nBFS traversal is:")
    ans = bfs(adj, start_node)
    for i in ans:
        print(i, end=" ")
