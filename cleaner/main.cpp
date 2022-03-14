#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include "scanner.h"
#include "token.h"

using namespace std;

int main(int argc, char* argv[])
{
	string filename = argv[1];

	vector<Token> tokens = Scanner(filename);
    
	return 0;
}