/*
https://www.nowcoder.com/questionTerminal/0425aa0df74646209d3f56f627298ab2

月神拿到一个新的数据集，其中每个样本都是一个字符串（长度小于100），样本的的后六位是纯数字，
月神需要将所有样本的后六位数字提出来，转换成数字，并排序输出。
月神要实现这样一个很简单的功能确没有时间，作为好朋友的你，一定能解决月神的烦恼，对吧。

每个测试用例的第一行是一个正整数M（1<=M<=100)，表示数据集的样本数目
接下来输入M行，每行是数据集的一个样本，每个样本均是字符串，且后六位是数字字符。

对每个数据集，输出所有样本的后六位构成的数字排序后的结果（每行输出一个样本的结果）
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
 
using namespace std;
 
int main(){
    int n,length;
    cin >> n;
    string input;
    string cnvt = "000000";
    vector<int> outputs;
    for (int i=0;i<n;i++) {
        cin >> input;
        length = input.size();
        cnvt[0] = input[length - 6];
        cnvt[1] = input[length - 5];
        cnvt[2] = input[length - 4];
        cnvt[3] = input[length - 3];
        cnvt[4] = input[length - 2];
        cnvt[5] = input[length - 1];
        outputs.push_back(atoi(cnvt.c_str()));
    }
    vector<int>::iterator it = outputs.begin();
    sort(it,it+n);
    for (int i=0;i<n;i++) {
        cout << outputs[i] << "\n";
    }
    return 0;
}