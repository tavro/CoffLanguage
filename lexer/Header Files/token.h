#pragma once
#include <iostream>
#include <string>

using namespace std;

class Token {
private:
	string _type;
	string _value;

public:
	Token(string type, string value);

	string getType();
	string getValue();

	bool isType(string type);
	bool isNumber();
	bool isDefinition();
	bool isString();
	bool isSymbol();
	bool isOperator();
	bool isAction();
	bool isEnd();

	void print();
	void set(string type, string value);
};
