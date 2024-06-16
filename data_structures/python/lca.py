class TreeAncestor:
    def __init__(self, edges):
        n = len(edges) + 1
        m = n.bit_length()
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        depth = [0] * n
        # pa[i][j]: 节点 i 嘅第 2^j 个祖先
        pa = [[-1] * m for _ in range(n)]
        
        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa
            for y in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    dfs(y, x)
        # 默认 0 系根节点, 从 0 开始
        dfs(0, -1)

        for i in range(m - 1):
            for x in range(n):
                p = pa[x][i]
                if p != -1:
                    pa[x][i + 1] = pa[p][i]
        
        self.depth = depth
        self.pa = pa

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k >> i) & 1:
                node = self.pa[node][i]
        return node

    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if x == y:
            return x
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py
        return self.pa[x][0]