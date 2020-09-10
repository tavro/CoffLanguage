#pragma once
#include "token.h";
#include <string>

using namespace std;

class Number : public Token {
private:
	int _intValue;

public:
	Number(int value);
	Number(string value);
	int getValue();
};