import lexerparser, interpreter

if __name__ == '__main__':
    parser = lexerparser.CoffParser()
    lexer = lexerparser.CoffLexer()
    env = {}
    instructions = []

    with open("program.coff") as file:
    	for line in file:
        	tree = parser.parse(lexer.tokenize(line))
        	if tree:
        		instructions.append(tree)
        		#print(tree)

prog = interpreter.CoffProgram()
prog.run_instructions(instructions)