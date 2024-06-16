class UnionFind:
    def __init__(self, n: int):
        self.pa = [i for i in range(n)]

    def find(self, x: int) -> int:
        if self.pa[x] == x:
            return x
        self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, x: int, y: int) -> None:
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.pa[px] = py