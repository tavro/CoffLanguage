#include "definition.h";

Definition::Definition(char value) : Token("definition", string(1, value))
{
	_charValue = value;
}

Definition::Definition(string value) : Token("definition", value)
{
	_charValue = value.at(0);
}

char Definition::getValue()
{
	return _charValue;
}