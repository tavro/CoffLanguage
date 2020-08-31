from sys import *

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
			token = ""
		elif token == ">":
			print("Print located")
			token = ""
		elif token == "\"":
			if state == 0:
				state = 1
			elif state == 1:
				print("String located")
				string = ""
				state = 0
		elif state == 1:
			string += c
			token = ""

def run():
	data = open_file("program.coff")
	lex(data)

run()