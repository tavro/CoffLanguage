#pragma once
#include "token.h";
#include <string>

using namespace std;

class Definition : public Token {
private:
	char _charValue;

public:
	Definition(char value);
	Definition(string value);
	char getValue();
};
