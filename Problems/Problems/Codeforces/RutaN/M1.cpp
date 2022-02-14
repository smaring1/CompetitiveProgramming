#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>


using namespace std;

int main()
{
    int t,cs;
    scanf("%d",&t);
    while(t--)
    {
        long long n,p;
        unsigned long long d,ans;
        scanf("%lld %lld %llu",&n,&p,&d);
        if(d<=n)
            printf("Case %d: 0\n",++cs);
        else
        {
            ans =ceil((double)(log(d)-log(n))/log(1+(p/100.0)));
            printf("Case %d: %llu\n",++cs,ans);
        }
    }
    return 0;
}