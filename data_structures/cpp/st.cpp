#include <iostream>
#include <cmath>
 
using namespace std;
 
const int mxn = 2e5 + 5;
int a[mxn];
 
struct ST {
  int ma[mxn][26];
  int mi[mxn][26];
  const int mxbit = 25;
 
  void build(int* a, int n) {
    for (int i = 1; i <= n; i++) {
      ma[i][0] = a[i];
      mi[i][0] = a[i];
    }
  
    for (int j = 1; j <= mxbit; j++) {
      for (int i = 1; i + (1 << j) - 1 <= n; i++) {
        ma[i][j] = max(ma[i][j - 1], ma[i + (1 << (j - 1))][j - 1]);
        mi[i][j] = min(mi[i][j - 1], mi[i + (1 << (j - 1))][j - 1]);
      }
    }
  }
  
  int query_max(int l, int r) {
    int x = (int)log2(r - l + 1);
    return max(ma[l][x], ma[r - (1 << x) + 1][x]);
  }
 
  int query_min(int l, int r) {
    int x = (int)log2(r - l + 1);
    return min(mi[l][x], mi[r - (1 << x) + 1][x]);
  }
} st;
 
int main() {
    // 建立表
    st.build(a, 10);
    // st.query_max(1, 5);
    // st.query_min(5, 7);
    return 0;
}