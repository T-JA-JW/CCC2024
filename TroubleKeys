#include <bits/stdc++.h>
using namespace std;




int main() {
    string s1, s2;
    cin >> s1 >> s2;
    bool silly=false;
    bool quiet=false;
    char sk='@', srk='%', qk='-';
    while (s1.size()!=s2.size()) {
        s2+=" ";
    }
    
    //find quiet first
    for (int i=0; i<s1.size(); i++) {
        if (s1[i]!=s2[i]) {
            if (s1.find(s2[i])!=-1) {
                if (quiet==false) {
                    qk=s1[i];
                    quiet=true;
                }
                
            }
            else if (s2[i]==' ' and quiet==false) {
                qk=s1[i];
                quiet=true;
            }
        }
    }
    //cout << qk;
    
    string news1="";
    for (int i=0; i<s1.size(); i++) {
        if (s1[i]!=qk) {
            news1+=s1[i];
        }
    }
    //cout << news1;
    
    //now find silly
    for (int i=0; i<news1.size(); i++) {
        if (news1[i]!=s2[i]) {
            sk=news1[i];
            srk=s2[i];
            break;
        }
    }
    
   cout << sk << " " << srk << "\n" << qk;
   
  
    
}
