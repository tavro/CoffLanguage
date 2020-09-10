#pragma once
#include "token.h";
#include <string>

using namespace std;

class End : public Token {
private:
	char _charValue;

public:
	End();
	char getValue();
};
