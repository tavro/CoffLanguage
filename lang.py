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
			elif expression != "" and not is_expression:
				tokens.append("NUMBER:" + expression)
				expression = ""
			elif var != "":
				tokens.append("VARIAB:" + var)
				var = ""
				var_started = False
			token = ""
		elif token == "=" and state == 0:
			if var != "":
				tokens.append("VARIAB:" + var)
				var = ""
				var_started = False
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
		elif len(token) == 1 and token.isdigit():
			expression += token
			token = ""
		elif token in "+-*/%()":
			is_expression = True
			expression += token
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
		if token_list[i] == "PRINT":
			print_line(token_list[i+1])
			i+=2
		elif token_list[i][0:6] + " " + token_list[i + 1] == "VARIAB EQUALS":
			if token_list[i + 2][0:6] == "STRING" or token_list[i + 2][0:6] == "NUMBER":
				assign_variable(token_list[i][7:], token_list[i+2])
				i+=3
			elif token_list[i + 2][0:6] == "EXPRES":
				assign_variable(token_list[i][7:], "NUMBER:" + str(eval(token_list[i+2][7:])))
				i+=3

def run():
	data = open_file("program.coff")
	token_list = lex(data)
	parse(tokens)

run()