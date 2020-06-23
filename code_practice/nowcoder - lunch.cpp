/*
https://www.nowcoder.com/questionTerminal/824af5cb05794606b56657bb3fa91f49

又到了吃午饭的时间，你和你的同伴刚刚研发出了最新的GSS-483型自动打饭机器人，现在你们正在对机器人进行功能测试。
为了简化问题，我们假设午饭一共有N个菜，对于第i个菜，你和你的同伴对其定义了一个好吃程度（或难吃程度，如果是负数的话……）A[i]，
由于一些技（经）术（费）限制，机器人一次只能接受一个指令：两个数L, R——表示机器人将会去打第L~R一共R-L+1个菜。
本着不浪费的原则，你们决定机器人打上来的菜，含着泪也要都吃完，于是你们希望机器人打的菜的好吃程度之和最大
然而，你善变的同伴希望对机器人进行多次测试（实际上可能是为了多吃到好吃的菜），他想知道机器人打M次菜能达到的最大的好吃程度之和
当然，打过一次的菜是不能再打的，而且你也可以对机器人输入-1, -1，表示一个菜也不打

输入:
第一行：N, M
第二行：A[1], A[2], ..., A[N]

输出一个数字S，表示M次打菜的最大好吃程度之和
*/

#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;
 
int main() {
    int n,m,temp;
    cin >> n >> m;
    if (n<1 || m<1) {
        printf("0");
        return 0;
    }
    vector<int> dishes;
    int input;
    temp = 0;
    for (int i=0;i<n;i++) {
        cin >> input;
        if (input > 0) {
            if (temp >= 0) {
                temp += input;
            }
            else {
                dishes.push_back(temp);
                temp = input;
            }
        }
        else if (input < 0) {
            if (temp <= 0) {
                temp += input;
            }
            else {
                dishes.push_back(temp);
                temp = input;
            }
        }
    }
    dishes.push_back(temp);
     
    vector<int>::iterator it = dishes.begin();
    if (dishes[0] <= 0) dishes.erase(it);
    if (dishes.size() == 0) {
        cout << 0;
        return 0;
    }
    it = dishes.end();
    if (*(it-1)<0) dishes.erase(it-1);
     
    if (dishes.size()<= 2*m - 1){
        temp = 0;
        for (int i=0;i<dishes.size();i++) {
            if (dishes[i]>0) temp += dishes[i];
        }
        cout << temp;
        return 0;
    }
     
    vector<int> count(m,0);
    vector<int> largest(m,0);
    count[0] = dishes[0];largest[0] = dishes[0];
    for (int i=1;i<dishes.size();i++) {
        for (int j=1;j<m;j++) {
            if (j>i) break;
            if (largest[j-1] >= count[j]) {
                count[j] = largest[j-1] + dishes[i];
            }
            else count[j] = count[j] + dishes[i];
        }
        if (count[0] < 0) count[0] = 0;
        count[0] = count[0] + dishes[i];
        for (int j=0;j<m;j++){
            if (j>i) break;
            if (largest[j] < count[j]) largest[j] = count[j];
        }
    }
     
    temp = 0;
    for (int i=0;i<m;i++) {
        if (largest[i] > temp) temp = largest[i];
    }
     
    cout << temp;
    return 0;
}