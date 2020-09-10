#include "end.h";

End::End() : Token("end", ".")
{
	_charValue = '.';
}

char End::getValue()
{
	return _charValue;
}