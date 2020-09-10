#include "action.h";

Action::Action(char value) : Token("action", string(1, value))
{
	_charValue = value;
}

Action::Action(string value) : Token("action", value)
{
	_charValue = value.at(0);
}

char Action::getValue()
{
	return _charValue;
}