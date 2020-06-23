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