#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

int main () {
    
    ifstream instream;
    ofstream outstream;
    string address1 = "C:\\test\\input_file.txt";
    string address2 = "C:\\test\\input_new.txt";
    instream.open(address1);
    outstream.open(address2);
    if (!instream.is_open()||!outstream.is_open()) { 
        cout << "Error opening file"; 
        exit (1); 
    }
    
    //start
    bool lineblind = false;
	bool allblind = false;
    bool extendblind = false;
    
    //int tmpl;

	char bufferin[100];
    string bufferout;

    int len;
    while (!instream.eof())
    {
        instream.getline(bufferin,100);
        len = instream.gcount();
        for (int i=0;i<len;i++) {
            lineblind = false;
            if (i < len - 1) {
                
                if (bufferin[i] == '/') {
                    
                    // case: short comment
                    if (bufferin[i+1] == '/') {
                        lineblind = true;
                    }
                    
                    // case: long comment start
                    else if (bufferin[i+1] == '*') {
                        allblind = true;
                    }
                }
                
                // case: long comment end
                if ((bufferin[i] == '*') && (bufferin[i+1] == '/')){
                    allblind = false;
                    extendblind = true;
                    continue;
                } 
            }
            if (lineblind||allblind||extendblind) {
                //if (extendblind) {
                    extendblind = false;
                //}
                continue;
            }
            else {
                bufferout += bufferin[i];
            }
        }
        //tmpl = bufferout.length();
        if (bufferout != "") {
            if (bufferout.length() == 1) {
                int d = (int)(bufferout[0]);
                if (d == 0) {
                    continue;
                }
                else {
                    outstream << bufferout << endl;
                }
            }
            else {
                outstream << bufferout << endl;
            }
            bufferout.clear();
        }
    }
    //cout << in.gcount() <<endl;
    //char testc = buffer[1];
    //cout << (buffer[1] == '\n') << endl;
    
    instream.close();
	outstream.close();

    return 0;
}

