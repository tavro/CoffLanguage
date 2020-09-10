#pragma once
#include "token.h";
#include <string>

using namespace std;

class Operator : public Token {
private:
	char _charValue;

public:
	Operator(char value);
	Operator(string value);
	char getValue();
};