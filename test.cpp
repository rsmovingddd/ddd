#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n,m,temp;
    scanf("%d %d",&n,&m);
    if (n == 1) {
        printf(0);
        return 0;
    }
    vector<int> vec;
    for (int i=0;i<n;i++) {
        scanf("%d",&temp);
        vec.push_back(temp);
    }
    
    vector<int>::iterator it = vec.begin();
    sort(it,it+n);
    int temp1,temp2,pos1,pos2;
    
    for (int i=0;i<m;i++) {
        temp1 = vec[0];
        temp2 = vec[n-1];
        if (temp1 >= temp2) break;
        pos1 = 1;pos2 = n-1;
        while (pos1<n-2) {
            if (vec[pos1] > temp1) {
                pos1--;
                break;
            }    
            pos1++;
        }
        if (pos1 == n-2 && n != 2 && n != 3) pos1--;
        while (pos2>1) {
            if (vec[pos2] < temp2) {
                pos2++;
                break;
            }
            pos2--;
        }
        if (pos2 == 1) pos2++;
        vec[pos1] += 1;vec[pos2] -= 1;
    }
    temp = vec[0]-vec[n-1];
    if (temp<0) temp = -temp;
    printf("%d",temp);
    
    return 0;
}