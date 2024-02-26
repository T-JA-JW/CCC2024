#include <bits/stdc++.h>
using namespace std;

int r, c;
vector<string>farm;
vector<vector<int>> check;
int dx[4]= {1, -1, 0, 0};
int dy[4]= {0, 0, 1, -1};

void dfs(int x, int y) {
    check[x][y]=1;
    for (int i=0; i<4; i++) {
        int nx=x+dx[i];
        int ny=y+dy[i];
        if (nx>=0 and ny>=0 and nx<r and ny<c) {
            if (check[nx][ny]==0 and farm[nx][ny]!='*') {
                dfs(nx, ny);
            }
        }
    }
}

int main() {
    cin >> r >> c;
    for (int i=0; i<r; i++) {
        string temp;
        cin >> temp;
        farm.push_back(temp);
    }
    for (int i=0; i<r+5; i++) {
        vector<int>ttemp;
        for (int j=0; j<c+5; j++) {
            ttemp.push_back(0);
        }
        check.push_back(ttemp);
    }
    int sr, sc;
    cin >> sr >> sc;
    dfs(sr, sc);
    
    long long ans=0;
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            if (check[i][j]==1) {
                char pump=farm[i][j];
                if (pump=='L') {
                    ans+=10;
                }
                else if (pump=='M') {
                    ans+=5;
                }
                else if (pump=='S') {
                    ans++;
                }
            }
        }
    }
    cout << ans;
  
    
}
