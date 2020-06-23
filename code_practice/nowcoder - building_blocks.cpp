/*
https://www.nowcoder.com/questionTerminal/55371b74b2f243e3820e57ee4c7b5504

小明有一袋子长方形的积木，如果一个积木A的长和宽都不大于另外一个积木B的长和宽，
则积木A可以搭在积木B的上面。好奇的小明特别想知道这一袋子积木最多可以搭多少层，你能帮他想想办法吗？
定义每一个长方形的长L和宽W都为正整数，并且1 <= W <= L <= INT_MAX, 袋子里面长方形的个数为N, 并且 1 <= N <= 1000000.

假如袋子里共有5个积木分别为 (2, 2), (2, 4), (3, 3), (2, 5), (4, 5), 则不难判断这些积木最多可以搭成4层, 
因为(2, 2) < (2, 4) < (2, 5) < (4, 5)。

输入第一行为积木的总个数 N。之后一共有N行，分别对应于每一个积木的宽W和长L

输出总共可以搭的层数
*/

#include <stdio.h>
#include <vector>
#include <utility>
#include <algorithm>
 
using namespace std;
 
bool sort1(pair<int,int> pair1,pair<int,int> pair2) {
    if (pair1.first == pair2.first) {
        return (pair1.second < pair2.second);
    }
     else return (pair1.first < pair2.first);
}
 
int main(){
    int n,temp1,temp2;
    scanf("%d",&n);
    pair<int,int> jm[n];
    for (int i=0;i<n;i++) {
        scanf("%d %d",&temp1,&temp2);
        jm[i].first = temp1;
        jm[i].second = temp2;
    }
    sort(jm,jm + n,sort1);
    int count[n];
    int len = 1;
    count[0] = jm[0].second;
    for (int i=1;i<n;i++) {
        if (jm[i].second >= count[len-1]) {
            count[len] = jm[i].second;
            len++;
        }
        else {
            *(upper_bound(count,count+len,jm[i].second)) = jm[i].second;
        }
    }
    printf("%d",len);
    return 0;
}