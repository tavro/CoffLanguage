from sys import *

tokens = []

def open_file(filename):
	data = open(filename, "r").read()
	return data

def lex(contents):
	token = ""
	state = 0
	string = ""
	contents = list(contents)
	for c in contents:
		token += c
		if token == " ":
			if state == 0:
				token = ""
		elif token == "\n":
			token = ""
		elif token == ">":
			tokens.append("PRINT")
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
		if token_list[i] + " " + token_list[i+1][0:6] == "PRINT STRING":
			print(token_list[i+1][7:])
			i+=2


def run():
	data = open_file("program.coff")
	token_list = lex(data)
	parse(tokens)

run()