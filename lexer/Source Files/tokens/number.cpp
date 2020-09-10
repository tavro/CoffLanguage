#include "number.h";

Number::Number(int value) : Token("number", to_string(value))
{
	_intValue = value;
}

Number::Number(string value) : Token("number", value) 
{
	_intValue = stoi(value);
}

int Number::getValue() 
{
	return _intValue;
}