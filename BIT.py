lowbit = lambda x : x & (-x)

class BIT:
    def __init__(self, n):
        self.tree = [0] * n

    def update(self, i: int, k: int) -> None:
        while i < len(self.tree):
            self.tree[i] += k
            i += lowbit(i)

    def sum(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= lowbit(i)
    
    def query(self, l: int, r: int) -> int:
        return self.sum(r) - self.sum(l - 1)