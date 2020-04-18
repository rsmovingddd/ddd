#include <iostream>
#include <fstream>
#include <string>
#include "songhan_q3.h"
using namespace std;

// Constants and Types
const string HEADER = "CSC3002 Assignment1 Question3: Remove Comments";
const string PROMPT_IN = "Enter abosulte input file path: ";
const string PROMPT_OUT = "The output file is: ";
const string ENDPRO = "End of Question3";

/*
 * Please add the function description
 */
void q3() {
    cout << HEADER << endl << PROMPT_IN;
    
	// f_path_temp: store the path read from console
	string f_path_temp;
	cin >> f_path_temp;
	//cout << "File path input is: " << f_path_temp << endl;
    
    // f_path_input: store the path of input file
	string f_path_input = f_path_temp;
    
    // get the output file path by modification to f_path_temp
	int pos = f_path_temp.length() - 8;
    f_path_temp.replace(pos,8,"new.txt");
    
	// f_path_out: store the path of input file
    string f_path_output = f_path_temp;
    
	// setting input and output file streams
	ifstream stream1;
	ofstream stream2;
	string state = readFileFromPath(stream1,  f_path_input); 
	stream2.open(f_path_output,ios::trunc);
	
	removeComments(stream1, stream2);

	stream1.close();
	stream2.close();
    
	cout << PROMPT_OUT << f_path_temp << endl;
	cout << ENDPRO << endl;
}

/*
 * Please add the function description
 */
void removeComments(istream & is, ostream & os) {
	bool last_digit_is_slash  = false;   //define a variable to check if the last element is hash, 
	                                    //if we read a hash, it will become true, otherwise it will returns false. 
	bool last_digit_is_star = false;
	bool double_slash_status = false;
	bool slash_star_status = false;

	while (char ch = is.get() != EOF)
	{
		if (ch == '/' && last_digit_is_slash == true)
		{
			double_slash_status = true;
			cout << "no";
		}
		else if (ch == '*' && last_digit_is_slash == true)
		{
			slash_star_status = true;
			cout << "no";
		}
		else if (ch == '/' && last_digit_is_star == true && slash_star_status==true)
		{
			slash_star_status = false;
			//cout << "no";
		}
		else if (ch == '/n' && double_slash_status == true)
		{
			double_slash_status = false;
			//cout << "yes";
			os<<ch;  //////////////////////////////////////////////////////////////////////
		}
		else if (last_digit_is_slash = true && (ch != '/' && ch != '*'))
		{
			is.unget();
			is.unget();
			char a = is.get();
			//cout << "yes";
			os<<a;  ///////////////////////////////////////////////////////////////////////
			is.get();
		}
		else if (ch != '/' && last_digit_is_star == false && slash_star_status == false) { os<<ch; }
		//cout << "yes";


		//myfile << "Writing this to a file.\n";
        
		if (ch == '/') { last_digit_is_slash = true; }
		else { last_digit_is_slash = false; }

		if (ch == '*') { last_digit_is_star = true; }
		else { last_digit_is_star = false; }
		
	}
    /*
     * Please add the function body
     */
}

/*
 *Please add the function description
 */
string readFileFromPath(ifstream & stream,  string f_path) {
	stream.open(f_path.c_str());
	if (!stream.fail()) { return f_path; }
	else {
        stream.clear();
	    cout << "Unable to open that file.  Try again." << endl;
		return "Unable to open that file.  Try again.";
	}
}


void main()
{
	q3();
}
