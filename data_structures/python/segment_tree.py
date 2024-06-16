# 线段树单点修改版本
def solve(nums):
    n = len(nums)
    val = [0] * (4 * n)

    def martain(o):
        val[o] = val[2 * o + 1] + val[2 * o]

    def do(o, v):
        val[o] += v

    def build(o, l, r):
        if l == r:
            val[o] = 0
            return
        m = (l + r) // 2
        build(o * 2, l, m)
        build(o * 2 + 1, m + 1, r)
        martain(o)

    def update(o, l, r, pos, v):
        if pos < l or pos > r:
            return
        if l == r and l == pos:
            do(o, v)
            return
        m = (l + r) // 2
        update(o * 2, l, m, pos, v)
        update(o * 2 + 1, m + 1, r, pos, v)
        martain(o) # 维护相关节点嘅更新

    def query(o, l, r, L, R):
        if r < L or l > R:
            return 0
        if L <= l and r <= R:
            return val[o]
        m = (l + r) // 2
        return query(o * 2, l, m, L, R) + query(o * 2 + 1, m + 1, r, L, R)

    build(1, 1, n)

solve()