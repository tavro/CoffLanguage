#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stdexcept>
#include <algorithm>
#include <tuple>
#include "token.h"

using std::string;
using std::vector;
using std::tuple;
using std::ifstream;
using std::find;
using std::endl;
using std::getline;
using std::cout;

vector<Token> lexer(vector<char> chars);

int main()
{
	ifstream file("input.txt");
	string line;

	vector<char> symbols;
	while (getline(file, line)) 
	{
		for (char symbol : line) 
		{
			symbols.push_back(symbol);
		}
	}

	vector<Token> tokens = lexer(symbols);
	for (Token token : tokens) 
	{
		token.print();
	}

	return 0;
}

string scan_symbol(char first_char, vector<char> chars, vector<char> allowed_chars)
{
	string value = "";
	for (char c : chars) 
	{
		if (find(allowed_chars.begin(), allowed_chars.end(), c) != allowed_chars.end())
		{
			value += c;
		}
		else 
		{
			return value;
		}
	}
	return value;
}

string scan_string(char first_char, vector<char> chars)
{
	string value = "";
	chars.erase(chars.begin());
	for (char c : chars) 
	{
		if (c == first_char) 
		{
			return value;
		}
		value += c;
	}
	return "";
}

vector<char> create_sublist(vector<char> l, int index) 
{
	vector<char> lis;
	for (int i = index; i < l.size(); i++)
	{
		lis.push_back(l.at(i));
	}
	return lis;
}

vector<Token> lexer(vector<char> chars)
{
	vector<Token> tokens;
	string number = "0123456789";
	string start = "?@#[";
	string end = ".";
	string special = "><=();:]{},!";
	string symbol = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_";
	for (int i = 0; i < chars.size(); i++)
	{
		if (chars.at(i) == ' ' || chars.at(i) == '\n' || chars.at(i) == '\t');
		else if (chars.at(i) == '+' || chars.at(i) == '-' || chars.at(i) == '*' || chars.at(i) == '/')
		{
			string t(1, chars.at(i));
			tokens.push_back(Token("operator", t));
		}
		else if (chars.at(i) == '\'' || chars.at(i) == '"')
		{
			string str = scan_string(chars.at(i), create_sublist(chars, i));
			tokens.push_back(Token("string", str));
			i += str.size()+1;
		}
		else if (number.find(chars.at(i)) != std::string::npos)
		{
			vector<char> allowed_characters;
			for (char& ch : number) {
				allowed_characters.push_back(ch);
			}
			string str = scan_symbol(chars.at(i), create_sublist(chars, i), allowed_characters);
			tokens.push_back(Token("number", str));
			i += str.size()-1;
		}
		else if (symbol.find(chars.at(i)) != std::string::npos)
		{
			vector<char> allowed_characters;
			for (char& ch : symbol) {
				allowed_characters.push_back(ch);
			}
			string str = scan_symbol(chars.at(i), create_sublist(chars, i), allowed_characters);
			tokens.push_back(Token("symbol", str));
			i += str.size()-1;
		}
		else if (special.find(chars.at(i)) != std::string::npos)
		{
			string t(1, chars.at(i));
			tokens.push_back(Token("special", t));
		}
		else if (start.find(chars.at(i)) != std::string::npos)
		{
			string t(1, chars.at(i));
			tokens.push_back(Token("start", t));
		}
		else if (end.find(chars.at(i)) != std::string::npos)
		{
			string t(1, chars.at(i));
			tokens.push_back(Token("end", t));
		}
		else
		{
			string t(1, chars.at(i));
			tokens.push_back(Token("undefined", t));
		}
	}
	return tokens;
}

