#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include "token.h"

vector<Token> Scanner(string filename)
{
	ifstream inFile;
	inFile.open(filename);
	vector<Token> tokens;
	int lineCount = 1;
	char tick = '3';
	char prev = '3';
	bool run = true;
	char temp = '3';
	int count = 0;
	int fileCount = 0;
	bool pass = false;
	string nonAlpha = ",.?()";
	string operation = "+-*";

	if (inFile.fail())
	{
		cerr << "Error opening file";
	}
	while (run) {

		fileCount++;
		ofstream myfile;
		string fileName = "d";
		fileName += std::to_string(fileCount);
		fileName += ".txt";
		cout << "Populating " << fileName << endl;
  		myfile.open (fileName);
  		
		count = 0;
		myfile << "[" << endl;
		if (pass) {
			myfile << "{";
		}
		while (count < 100)
		{
			temp = inFile.get();
				
			if (temp == EOF) {
				run = false;
				count = 11;
			}

			else if (!isspace(temp)) {
				if ((temp != ' ' && temp != '\n')) {
					prev = tick;
					tick = temp;
					if (prev == '}' && tick == '{') {
						count++;
						if (count < 20) {
							myfile << "," << tick;
						}
					}

					else {
						myfile << tick;
					}
					
				}
				
			}
			else {
				myfile << temp;
			}
			


		}
		myfile << "]";
		pass = true;
		myfile.close();
	}

	cout << endl << endl << endl << "File Count: " << fileCount << endl;
	

	return tokens;
}