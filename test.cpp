#include <stdio.h>
#include <vector>

using namespace std;

int main() {
    int t,temp,n,temp2;
    scanf("%d",&t);
    vector<int> pos,wei,vec;
    vector<int> result;
    for (int cc = 0;cc<t;cc++) {
        scanf("%d",&n);
        for (int i = 0;i<n;i++) {
            scanf("%d",&temp);
            pos.push_back(temp);
        }
        for (int i = 0;i<n;i++) {
            scanf("%d",&temp);
            wei.push_back(temp);
        }
        
        if (n%2 == 0) {
            temp = 0;
            for (int i = 0;i<n;i++) {
                temp += wei[i];
            }
            result.push_back(temp);
        }
        else {
            /*
            for (int i = 0;i<n;i++) {
                vec.push_back(0);
            }
            for (int i = 0;i<n;i++) {
                vec[ (pos[i]) ] = wei[i];
            }
            */
            temp = 0;
            temp2 = 101;
            for (int i = 0;i<n;i++) {
                temp += wei[i];
                if (wei[i] < temp2) temp2 = wei[i];
            }
            result.push_back(temp + temp2);
        }
        for (int i = 0;i<n;i++) {
            pos.pop_back();wei.pop_back();
        }
    }
    
    for (int i=0;i<t;i++) {
        printf("%d\n",result[i]);
    }
    
    return 0;
}