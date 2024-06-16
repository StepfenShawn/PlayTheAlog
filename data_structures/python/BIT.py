lowbit = lambda x : x & (-x)
class BIT:
    def __init__(self, n):
        self.tree = [0] * n
    
    def update(self, i: int, k: int):
        while i < len(self.tree):
            self.tree[i] += k
            i += lowbit(i)
    
    def sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= lowbit(i)
        return res
    
    def query(self, l, r):
        return self.sum(r) - self.sum(l - 1)