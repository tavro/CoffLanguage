#include "token.h"

Token::Token(string type = "", string value = "")
{
	set(type, value);
}

string Token::getType()
{
	return _type;
}

string Token::getValue()
{
	return _value;
}

void Token::print()
{
	cout << "(" << _type << ", " << _value << ")" << endl;
}

void Token::set(string type, string value) 
{
	_type = type;
	_value = value;
}

bool Token::isType(string type)
{
	return (_type == type);
}

bool Token::isNumber() 
{
	return (_type == "number");
}

bool Token::isDefinition()
{
	return (_type == "definition");
}

bool Token::isSymbol()
{
	return (_type == "symbol");
}

bool Token::isString()
{
	return (_type == "string");
}

bool Token::isAction()
{
	return (_type == "action");
}

bool Token::isOperator()
{
	return (_type == "operator");
}

bool Token::isEnd()
{
	return (_type == "end");
}