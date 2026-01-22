class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # undirected

        visited = [False] * n
        q = deque([source])
        visited[source] = True

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

        return False
        