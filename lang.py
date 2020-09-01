from sys import *

tokens = []
symbols = {}

def print_line(o):
	if o[0:6] == "STRING":
		print(o[8:-1])
	elif o[0:6] == "NUMBER" or o[0:6] == "EXPRES":
		print(eval(o[7:]))
	elif o[0:6] == "VARIAB":
		print_line(get_variable(o[7:]))

def assign_variable(n, v):
	symbols[n] = v

def get_variable(n):
	if n in symbols:
		return symbols[n]
	else:
		return None

def get_input(n):
	i = input()
	symbols[n] = "STRING:\"" + i + "\""

def open_file(filename):
	data = open(filename, "r").read()
	data += "\n"
	return data

def lex(contents):

	token = ""
	string = ""
	expression = ""
	number = ""
	var = ""

	state = 0

	is_expression = False
	var_started = False

	contents = list(contents)
	for c in contents:
		token += c
		if token == " ":
			if state == 0:
				token = ""
		elif token == "\n":
			if expression != "" and is_expression:
				tokens.append("EXPRES:" + expression)
				expression = ""
				is_expression = False;
			elif expression != "" and not is_expression:
				tokens.append("NUMBER:" + expression)
				expression = ""
			elif var != "":
				tokens.append("VARIAB:" + var)
				var = ""
				var_started = False
			token = ""
		elif token == "=" and state == 0:
			if expression != "" and not is_expression:
				tokens.append("NUMBER:" + expression)
				expression = ""
			if var != "":
				tokens.append("VARIAB:" + var)
				var = ""
				var_started = False
			if tokens[-1] == "EQUALS":
				tokens[-1] = ("EQUEQU")
			else:
				tokens.append("EQUALS")
			token = ""
		elif token == "$" and state == 0:
			var_started = True
			var += token
			token = ""
		elif var_started:
			var += token
			token = ""
		elif token == ">":
			tokens.append("PRINT")
			token = ""
		elif token == "<":
			tokens.append("INPUT")
			token = ""
		elif token == ";":
			tokens.append("ENDIF")
			token = ""
		elif token == "if[":
			tokens.append("IF")
			token = ""
		elif token == "]":
			if expression != "" and not is_expression:
				tokens.append("NUMBER:" + expression)
				expression = ""
			tokens.append("THEN")
			token = ""
		elif len(token) == 1 and token.isdigit():
			expression += token
			token = ""
		elif token in "+-*/%()":
			is_expression = True
			expression += token
			token = ""
		elif token == "\t":
			token = ""
		elif token == "\"":
			if state == 0:
				state = 1
			elif state == 1:
				tokens.append("STRING:" + string + "\"")
				string = ""
				state = 0
				token = ""
		elif state == 1:
			string += token
			token = ""
	return tokens

def parse(token_list):
	i = 0
	while i < len(token_list):
		if token_list[i] == "ENDIF":
			i+=1
		elif token_list[i] == "PRINT":
			print_line(token_list[i+1])
			i+=2
		elif token_list[i][0:6] + " " + token_list[i + 1] == "VARIAB EQUALS":
			if token_list[i + 2][0:6] == "STRING" or token_list[i + 2][0:6] == "NUMBER":
				assign_variable(token_list[i][7:], token_list[i+2])
			elif token_list[i + 2][0:6] == "EXPRES":
				assign_variable(token_list[i][7:], "NUMBER:" + str(eval(token_list[i+2][7:])))
			elif token_list[i + 2][0:6] == "VARIAB":
				assign_variable(token_list[i][7:], get_variable(token_list[i+2][7:]))
			i+=3
		elif token_list[i] + " " + token_list[i + 1][0:6] == "INPUT VARIAB":
			get_input(token_list[i + 1][7:])
			i+=2
		elif token_list[i] + " " + token_list[i + 1][0:6] + " " + token_list[i + 2] + " " + token_list[i + 3][0:6]  + " " + token_list[i + 4]== "IF NUMBER EQUEQU NUMBER THEN":
			if token_list[i + 1][7:] == token_list[i + 3][7:]:
				pass
			else:
				pass
			i+=5

def run():
	data = open_file("program.coff")
	tokens = lex(data)
	parse(tokens)

run()