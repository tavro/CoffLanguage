#include "operator.h";

Operator::Operator(char value) : Token("operator", string(1, value))
{
	_charValue = value;
}

Operator::Operator(string value) : Token("operator", value)
{
	_charValue = value.at(0);
}

char Operator::getValue()
{
	return _charValue;
}