from sys import *

tokens = []

def print_line(o):
	if o[0:6] == "STRING":
		print(o[8:-1])
	elif o[0:6] == "NUMBER" or o[0:6] == "EXPRES":
		print(o[7:])

def open_file(filename):
	data = open(filename, "r").read()
	data += "\n"
	return data

def lex(contents):

	token = ""
	string = ""
	expression = ""
	number = ""

	state = 0

	is_expression = False
	
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
			token = ""
		elif token == ">":
			tokens.append("PRINT")
			token = ""
		elif len(token) == 1 and token.isdigit():
			expression += token
			token = ""
		elif token in "+-*/()":
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

def run():
	data = open_file("program.coff")
	token_list = lex(data)
	parse(tokens)

run()