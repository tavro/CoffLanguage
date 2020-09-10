#pragma once
#include <vector>
#include <string>

using namespace std;

class Block
{
private:
	string _startTag;
	vector<string> _tokens;
	vector<Block> _blocks;
	string _endTag;
public:
	Block(string startTag);
	void addBlock(Block block);
	void addToken(string token);
	void printTokens();
	int getBlockSize();
};