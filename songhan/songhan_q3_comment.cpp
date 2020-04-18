#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include "songhan_q3.h"
using namespace std;

// Constants and Types
const string HEADER = "CSC3002 Assignment1 Question3: Remove Comments";
const string PROMPT_IN = "Enter abosulte input file path: ";
const string PROMPT_OUT = "The output file is: ";
const string ENDPRO = "End of Question3";

/*
 * function: q3
 * console input: a C++ file, in a certain location. Its name MUST BE "input_file.txt"
 * console output: a C++ file, in a same location as the previous file, with name "input_new.txt"
 * usage: set up basic environments, and test function removeComments()
 */
void q3() {
    cout << HEADER << endl << PROMPT_IN;
    
	//* f_path_temp: path read from console
	string f_path_temp;
	cin >> f_path_temp;
	//cout << "File path input is: " << f_path_temp << endl;
    
    //* f_path_input: path of input file
	string f_path_input = f_path_temp;
    
    //* modify f_path_temp
	int pos = f_path_temp.length() - 8;
    f_path_temp.replace(pos,8,"new.txt");
    
	//* f_path_out: path of file
    string f_path_output = f_path_temp;
    
	//* setting input and output file streams
	ifstream stream1;
	ofstream stream2;
	string state1 = readFileFromPath(stream1,  f_path_input); 
	stream2.open(f_path_output,ios::trunc);
	
	removeComments(stream1, stream2);

	stream1.close();
	stream2.close();
    
    //* console output
	cout << PROMPT_OUT << f_path_temp << endl;
	cout << ENDPRO << endl;
}

/*
 * function: removeComments
 * function input: the reference of input file stream (read from certain input file)
 * function output: the reference of output file stream (write to certain output file)
 * usage: send a copy of input file to output file, with all the comments removed
 */
void removeComments(istream & instream, ostream & outstream) {
    
    //* lineblind: the flag used with case of line comment, false when inactivated
	bool lineblind = false;
    //* lineblind: the flag used with case of long comment, false when inactivated
    bool allblind = false;
    //* extendblind: the extensive flag used for "*/", false when inactivated
    bool extendblind = false;
    
    //int tmpl;
    string tmpstring;
    
    //* bufferin: buffer used to store single lines received from input stream
	char bufferin[100];
    //* bufferout: buffer used to store strings, before writing into output file line by line
    string bufferout;
    //* len: length of the number of chars actually received from input stream
    int len;
    
    while (!instream.eof())
    {
        //* for the beginning of each dealing of line, reset line comment state
        lineblind = false;
        
        //* bufferin receive from input stream
        instream.getline(bufferin,100);
        len = instream.gcount();
        
        //* dealing with each char
        for (int i=0;i<len;i++) {
            if (i < len - 1) {
                
                if (bufferin[i] == '/') {
                    
                    //* case: short comment
                    if (bufferin[i+1] == '/') {
                        lineblind = true;
                    }
                    
                    //* case: long comment starts
                    else if (bufferin[i+1] == '*') {
                        allblind = true;
                    }
                }
                
                // case: long comment ends
                if ((bufferin[i] == '*') && (bufferin[i+1] == '/')){
                    allblind = false;
                    //* for "*/", both 2 char require igonrance
                    //* so a flag set up to help ignore the next '/'
                    extendblind = true;
                    continue;
                } 
            }
            //* line comment: ignore rest parts in the line
            if (lineblind) {
                break;
            }
            //* long comment: keep ignoring
            else if (allblind||extendblind) {
                //if (extendblind) {
                    extendblind = false;
                //}
                continue;
            }
            //* write char to bufferout
            else {
                bufferout += bufferin[i];
            }
        }
        //tmpl = bufferout.length();
        
        //* write bufferout to output stream
        if (bufferout != "") {
            
            /*
             * a special case is detected. Sometimes there would be a line of string, after converting, 
             * has length 1, and contain the single ASCII code "null". This would result in an
             * additional line. If the line, after converting, has only one char, it would be tested to
             * prevent the case
             */
            if (bufferout.length() == 1) {
                int d = (int)(bufferout[0]);
                if (d == 0) {
                    continue;
                }
                else if (bufferout != " "){
                    outstream << bufferout << endl;
                }
            }

            /*
             * another possible special case: Sometimes there would be a line full of empty spaces. 
             * In order to test the case, empty space at the tail of the converted line would be 
             * removed. If the string left has nothing, then it would obviously be the case
             */
            else {
                tmpstring = bufferout;
                tmpstring.erase(tmpstring.find_last_not_of(" ") + 1);
                if (tmpstring.length() != 0) {
                    outstream << bufferout << endl;
                }
            }
            
            //* clear bufferout for the next round
            bufferout.clear();
        }
    }
}

/*
 * function: readFileFromPath
 * function input: the reference of input file stream, and the path of input file
 * function output: whether the reading is successful
 * usage: read the file, and feed back whether successful
 */
string readFileFromPath(ifstream & stream,  string f_path) {
	stream.open(f_path);
	if (!stream.fail()) { return f_path; }
	else {
        stream.clear();
	    cout << "Unable to open that file.  Try again." << endl;
		return "Unable to open that file.  Try again.";
	}
}


int main()
{
	q3();
	return 0;
}
