#include <bits/stdc++.h>

using namespace std;

vector<int> stu;


int main() {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        int sc;
        cin >> sc;
        stu.push_back(sc);
    }
    sort(stu.begin(), stu.end());
    int cnt=1;
    int prev=stu[n-1];
    for (int i=n-2; i>=0; i--) {
        if (stu[i]==prev) continue;
        
        prev=stu[i];
        cnt++;
        if (cnt==3) break;
        
    }
    int ans=0;
    
    for (int i=0; i<n; i++) {
        if (stu[i]==prev) ans++;
    }
    
    cout << prev << " " << ans;
    
}
