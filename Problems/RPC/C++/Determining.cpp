#include <bits/stdc++.h>

#define D(x) cout << #x << ": " << x << endl;
#define forn(i,n) for(int i=0; i< (int)n; i++)
#define for1(i,n) for(int i=1; i<= (int)n; i++)
#define all(v) v.begin(),v.end()

using namespace std;

typedef long long ll;


long double f[10001];
long long f2[10001];

void fibo(){
    for(int i = 2; i < 10001; i++) {
        f[i] = f[i - 1] + f[i - 2];
        f2[i] = fmod(f[i] , 2147483647);
    } 
}

int Search(int l, int r, int n) {
    if (r >= l) { 
        int mid = l + (r - l) / 2; 

        if (f2[mid] == n){
            return n;
        }
        
        if (f2[mid] > n){ 
            return Search(l, mid - 1, n); 
        }
        return Search(mid + 1, r, n); 
    } 
    return -1; 
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);
    cout<< setprecision(20)<< fixed;
    #ifdef LOCAL
        freopen("input.txt", "r", stdin);
    #else
        #define endl '\n'
    #endif
    f[0] = 0;
    f[1] = 1;
    f2[0] = 0;
    f2[1] = 1;
    fibo();
    sort(f2, f2 + 10000);
    int t,aux;
    int n;
    cin >> t;
    forn(i,t){
        cin >> n;
        aux = Search(0,10000,n);
        if (aux == n){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
    }

    return 0;
}