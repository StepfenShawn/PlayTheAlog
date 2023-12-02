#include <string>
#include <iostream>

using namespace std;

constexpr int N = 1e5;

struct Trie
{
    int son[N][26];
    int num[N];
    int idx = 0;

    void build()
    {
        memset(son, 0, sizeof son);
        memset(num, 0, sizeof num);
    }

    void add(string str, int v) {
        int u = 0;
        for (int i = 0; i < str.size(); i++) {
            int j = str[i] - 'a';
            if (!son[u][j]) {
                son[u][j] = ++idx;
            }
            u = son[u][j];
        }
        num[u] += v;
    }

    void del(string str, int v) {
        add(str, -v);
    }

    int query(string str) {
        int u = 0;
        for (int i = 0; i < str.size(); i++) {
            int j = str[i] - 'a';
            if (!son[u][j]) return 0;
            u = son[u][j];
        }
        return num[u];
    }
};