/*
https://www.nowcoder.com/questionTerminal/93f2c11daeaf45959bb47e7894047085

小易觉得高数课太无聊了，决定睡觉。不过他对课上的一些内容挺感兴趣，所以希望你在老师讲到有趣的部分的时候叫醒他一下。
你知道了小易对一堂课每分钟知识点的感兴趣程度，并以分数量化，以及他在这堂课上每分钟是否会睡着，
你可以叫醒他一次，这会使得他在接下来的k分钟内保持清醒。你需要选择一种方案最大化小易这堂课听到的知识点分值。

输入描述:
第一行 n, k (1 <= n, k <= 105) ，表示这堂课持续多少分钟，以及叫醒小易一次使他能够保持清醒的时间。
第二行 n 个数，a1, a2, ... , an(1 <= ai <= 104) 表示小易对每分钟知识点的感兴趣评分。
第三行 n 个数，t1, t2, ... , tn 表示每分钟小易是否清醒, 1表示清醒。

输出描述:
小易这堂课听到的知识点的最大兴趣值。
*/

#include <stdio.h>
#include <vector>
 
using namespace std;
 
int main() {
    int n,k,temp;
    scanf("%d %d",&n,&k);
    vector<int> kno;
    for (int i=0;i<n;i++) {
        scanf("%d",&temp);
        kno.push_back(temp);
    }
    vector<int> nawk(n,0);
    int summing = 0;
    for (int i=0;i<n;i++) {
        scanf("%d",&temp);
        if (temp == 0) {
            nawk[i] = kno[i];
        }
        else summing += kno[i];
    }
    vector<int> bnf(n,0);
    //int it = 0;
    for (int i=0;i<k;i++){
        if (i == n) break;
        bnf[0] += nawk[i];
    }
    int it = 1;
    while (it<n-k+1) {
        bnf[it] += bnf[it-1] - nawk[it-1] + nawk[it+k-1];
        it++;
    }
    int result = 0;
    for (int i=0;i<it;i++) {
        if (result < bnf[i]) result = bnf[i];
    }
    printf("%d",result + summing);
    return 0;
}