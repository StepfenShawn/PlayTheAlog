const int MAXN = 100010; // 注意树状数组最大空间一般开到 1e5 + 10
#define lowbit(x) (x & -x)

int a[MAXN]; // 原数组
int c[MAXN]; // 树状数组
int n;  // 题目所给的数组 A 数据长度
struct BIT {
    // 查询区间 [1, x] 的和
    int query(int x)
    {
        int ans = 0;
        for(int i = x; i ; i -= lowbit(i))
            ans += c[i];
    
        return ans;
    }
    //修改位置 x 的值
    void add(int x, int v)
    {
        for(int i = x; i < MAXN; i += lowbit(i))
            c[i] += v;
    }
    // 初始化, 这里我选用O(nlogn)的方式
    void build()
    {
        for(int i = 1; i <= n; i ++ )
            add(i, a[i]);
    }
} bitTree;

int main() {
    bitTree.build();
    // ...
    return 0;
}