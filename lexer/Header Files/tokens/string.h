#pragma once
#include "token.h";
#include <string>

using namespace std;

class String : public Token {
public:
	String(string str);
};