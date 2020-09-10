#pragma once
#include "token.h";
#include <string>

using namespace std;

class Action : public Token {
private:
	char _charValue;

public:
	Action(char value);
	Action(string value);
	char getValue();
};