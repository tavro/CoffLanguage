#include <iostream>
#include "block.h";

Block::Block(string startTag) 
{
	_startTag = "START_" + startTag;
	_endTag = "END_" + startTag;
}

void Block::addBlock(Block block) 
{
	_blocks.push_back(block);
}

void Block::addToken(string token)
{
	_tokens.push_back(token);
}

void Block::printTokens() 
{
	for (string instruction : _tokens) 
	{
		cout << instruction << endl;
	}
}

int Block::getBlockSize() 
{
	return _blocks.size();
}