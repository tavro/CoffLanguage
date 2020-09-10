#pragma once
#include "token.h";
#include <string>

using namespace std;

class Symbol : public Token {
public:
	Symbol(string symbol);
};