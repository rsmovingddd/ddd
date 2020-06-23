/*
https://www.nowcoder.com/questionTerminal/5de228846bde4f399c4cd5672a1cf682

latex自然是广大研究人员最喜欢使用的科研论文排版工具之一。
月神想在iPhone 上查阅写好的paper，但是无赖iPhone 上没有月神喜欢使用的阅读软件，于是月神也希望像tex老爷爷Donald Knuth那样自己动手do it yourself一个。
在DIY这个阅读软件的过程中，月神碰到一个问题，已知iPhone屏幕的高为H，宽为W，若字体大小为S(假设为方形），则一行可放W / S(取整数部分）个文字，一屏最多可放H / S （取整数部分）行文字。
已知一篇paper有N个段落，每个段落的文字数目由a1, a2, a3,...., an表示，月神希望排版的页数不多于P页（一屏显示一页），那么月神最多可使用多大的字体呢？

1 <= W, H, ai <= 1000
1 <= P <= 1000000

每个测试用例的输入包含两行。
第一行输入N,P,H,W
第二行输入N个数a1,a2,a3,...,an表示每个段落的文字个数。

对于每个测试用例，输出最大允许的字符大小S
*/

#include <stdio.h>
#include <vector>
using namespace std;
 
int main(){
    int n,p,h,w;
    int temp;
    scanf("%d %d %d %d",&n,&p,&h,&w);
    vector<int> parts;
    for (int i=0;i<n;i++) {
        scanf("%d",&temp);
        parts.push_back(temp);
    }
    if (h==0||w==0) {
        printf("0");
        return 0;
    }
    long long width,height,sum,pages;
    int large = 1;
    while (true) {
        width = w/large; height = h/large;
        if (width==0||height==0) break;
        sum = 0;
        for (int i=0;i<n;i++) {
            sum += parts[i]/width;
            if (parts[i]%width != 0) sum++;
        }
        pages = sum/height;
        if (sum%height != 0) pages++;
        if (pages > p) break;
        large++;
    }
    printf("%d",large-1);
    return 0;
}