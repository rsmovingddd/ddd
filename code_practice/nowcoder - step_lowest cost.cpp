/*
https://www.nowcoder.com/questionTerminal/355885694012495281f415387db22fde

你需要爬上一个N层的楼梯，在爬楼梯过程中， 每阶楼梯需花费非负代价，第i阶楼梯花费代价表示为cost[i]， 
一旦你付出了代价，你可以在该阶基础上往上爬一阶或两阶。
你可以从第 0 阶或者 第 1 阶开始，请找到到达顶层的最小的代价是多少。
N和cost[i]皆为整数，且N∈[2,1000]，cost[i]∈ [0, 999]。
*/

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
 
using namespace std;
 
int main() {
    string input;
    getline(cin,input);
    //cout << input << "\n";
     
    int temp = input.size();
    for (int i=0;i<temp;i++) {
        if (input[i] == ',') input[i] = ' ';
    }
    //cout << input  << "\n";
    stringstream ss(input);
    vector<int> vec;
    while (ss >> temp) {
        vec.push_back(temp);
        //cout << temp << " ";
    }
    temp = vec.size();
    vec.push_back(0);vec.push_back(0);vec.push_back(0);
    int step = -1;
    int result = 0;
    while (step < temp) {
        if (vec[step+2] <= vec[step+1]) {
            result += vec[step+2];
            step += 2;
        }
        else if (vec[step+3] >= vec[step+2]) {
            result += vec[step+2];
            step += 2;
        }
        else {
            result += vec[step+1];
            step += 1;
        }
    }
    cout << result;
    return 0;
}