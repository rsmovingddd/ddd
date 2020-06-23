/*
https://www.nowcoder.com/questionTerminal/20c8731629b64109825595c3d349d2fc

请实现一个函数，功能为合并两个升序数组为一个升序数组
输入有多个测试用例，每个测试用例有1-2行，每行都是以英文逗号分隔从小到大排列的数字
输出一行以英文逗号分隔从小到大排列的数组
*/

#include <iostream>
#include <string>
#include <vector>
 
using namespace std;
 
void transform(string str, vector<int>& vec){
    int temp = 0;
    for(int i = 0; i < str.size(); ++i){
        if(str[i] >= '0' && str[i] <= '9'){
            temp = temp * 10 + str[i] - '0';
        }else{
            vec.push_back(temp);
            temp = 0;
        }
    }
    vec.push_back(temp);
}
 
int main(){
  
    string str1, str2;
    cin >> str1 >> str2;
    if(str1.size() == 0){
        cout << str2 << endl;
        return 0;
    }
    if(str2.size() == 0){
        cout << str1 << endl;
        return 0;
    }
    vector<int> arr1, arr2;
    transform(str1, arr1);
    transform(str2, arr2);
    int i = 0, j = 0;
    vector<int> res;
    while(i < arr1.size() && j < arr2.size()){
        if(arr1[i] < arr2[j]){
            res.push_back(arr1[i]);
            ++i;
        }else{
            res.push_back(arr2[j]);
            ++j;
        }
    }
    while(i < arr1.size()){
        res.push_back(arr1[i]);
        ++i;
    }
    while(j < arr2.size()){
        res.push_back(arr2[j]);
        ++j;
    }
    for(int i = 0; i < res.size() - 1; ++i){
        cout << res[i] << ",";
    }
    cout << res.back() << endl;
    return 0;
}