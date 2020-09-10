#include <iostream>
#include <vector>
#include <string>
#include "block.h"

using namespace std;

void parse(Block& block, vector<string> instructions)
{
	int endsToPass = -1;
	bool isFirstTime = true;
	Block tempBlock("TEMP");
	for (string instruction : instructions)
	{
		if (instruction == "definition")
		{
			//AT START
			tempBlock = Block("DEF");
			if (isFirstTime) 
			{
				block.addToken("GO TO DEF");
				isFirstTime = false;
			}
			endsToPass++;
		}
		else if (instruction == "end")
		{
			if (endsToPass == 0)
			{
				//REACHED END
				isFirstTime = true;
				block.addBlock(tempBlock);
				block.addToken("GO BACK FROM DEF");
				endsToPass = -1;
			}
			else
			{
				//NOT AT END
				tempBlock.addToken(instruction);
				endsToPass--;
			}
		}
		else
		{
			if (endsToPass == -1)
			{
				//NOT STARTED / HAS ENDED
				block.addToken(instruction);
			}
		}
	}
}

int main() 
{
	vector<string> instructions;
	Block program("PROGRAM");

	parse(program, instructions);

	return 0;
}

