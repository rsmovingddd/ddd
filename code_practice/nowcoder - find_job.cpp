/*
链接：https://www.nowcoder.com/questionTerminal/46e837a4ea9144f5ad2021658cb54c4d

为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力值的情况下，
牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，
牛牛依然使用自己的标准来帮助小伙伴们。牛牛的小伙伴太多了，于是他只好把这个任务交给了你。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
保证不存在两项工作的报酬相同。

输出描述:
对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。一个工作可以被多个人选择。
*/

#include <vector>
#include <iostream>
#include <map>
#include <algorithm>
#include <stdio.h>
 
using namespace std;
 
bool mode(pair<int,int> i,pair<int,int> j) {
    return (i.second < j.second);
}
 
int main(){
    int m,n;
    scanf("%d %d",&n,&m);
    map<int,int> mp;
    vector<pair<int,int> > member(m),result(m);
    int temp1, temp2;
     
    for (int i=0;i<n;i++) {
        scanf("%d %d",&temp1,&temp2);
        if (mp[temp1]<temp2) mp[temp1] = temp2;
    }
    for (int i=0;i<m;i++) {
        scanf("%d",&temp1);
        member[i] = make_pair(i,temp1);
    }
    vector<pair<int,int> >::iterator it = member.begin();
    sort(it,it+m,mode);
    for (int i=0;i<m;i++) result[i].second = member[i].first;
     
     
    map<int,int>::iterator mpit,mpend;
    mpit = mp.begin();
    mpend = mp.end();
    temp2 = 0;
    ///*
     
    while (mpit != mpend && temp2 < m) {
        if (mpit->first <= member[temp2].second){
            if (result[temp2].first < mpit->second)
                result[temp2].first = mpit->second;
                //printf("temp2 %d\n",result[temp2].first);
            mpit++;
            //printf("mpit++\n");
        }
        else{
            if (temp2 < m-1)
                result[temp2+1].first = result[temp2].first;
            temp2++;
            //printf("temp2++\n");
        }
    }
    ///*
    if (result[m-1].first == 0) {
        while (temp2 < m) {
            result[temp2].first =
                result[temp2 - 1].first;
            temp2++;
        }
    }
    it = result.begin();
    sort(it,it+m,mode);
    for (int i=0;i<m;i++) printf("%d\n",result[i]);
    //*/
}