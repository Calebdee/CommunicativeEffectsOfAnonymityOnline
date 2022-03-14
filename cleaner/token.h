#ifndef TOKEN
#define TOKEN
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

enum TokenType {COMMA, PERIOD, Q_MARK, LEFT_PAREN, RIGHT_PAREN, COLON, COLON_DASH, MULTIPLY, 
				ADD, SCHEMES, FACTS, RULES, QUERIES, ID, STRING, COMMENT, UNDEFINED, EOFILE};

class Token
{
private:
	string type;
	string value;
	int lineNum;

public:
	Token(string tempType, string tempValue, int tempNum)
	{
		type = tempType;
		value = tempValue;
		lineNum = tempNum;
	}

	string tokenToString(TokenType tok)
	{
		switch(tok)
		{
			case COMMA: 
				return "COMMA";
			case PERIOD:
				return "PERIOD";
			case Q_MARK:
				return "Q_MARK";
			case LEFT_PAREN:
				return "LEFT_PAREN";
			case RIGHT_PAREN:
				return "RIGHT_PAREN";
			case COLON:
				return "COLON";
			case COLON_DASH:
				return "COLON_DASH";
			case MULTIPLY:
				return "MULTIPLY";
			case ADD:
				return "ADD";
			case SCHEMES:
				return "SCHEMES";
			case FACTS:
				return "FACTS";
			case RULES:
				return "RULES";
			case QUERIES:
				return "QUERIES";
			case ID:
				return "ID";
			case STRING:
				return "STRING";
			case COMMENT:
				return "COMMENT";
			case UNDEFINED:
				return "UNDEFINED";
			case EOFILE:
				return "EOF";
		}

		return "UNDEFINED";
	}

	string toString()
	{
		std::stringstream out;
		out << "(" << type << "," << "\"" << value << "\"" << "," << lineNum << ")" << std::endl;
		return out.str();
	}
};
#endif // TOKEN