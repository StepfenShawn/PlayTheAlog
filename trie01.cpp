#include <string>
#include <iostream>

using namespace std;

constexpr int N = 1e5;

struct Trie01
{
    int son[N][2];
    int num[N];
    int idx = 0;

    void build()
    {
        memset(son, 0, sizeof son);
        memset(num, 0, sizeof num);
    }

    void add(int x) {
        int u = 0;
        for (int i = 30; i >= 0; i--) {
            int& s = son[u][(x >> i) & 1];
            if (!s) 
                s = ++idx;
            u = s;
        }
    }

    int query(int x) {
        int u = 0;
        int res = 0;

        for (int i = 30; i >= 0; i--) {
            int s = x >> i & 1;
            if (son[u][!s]) {
                res += 1 << i;
                u = son[u][!s];
            } else {
                u = son[u][s];
            }
        }

        return res;
    }
};