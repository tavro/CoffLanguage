class CoffProgram():
	@staticmethod
	def run_instructions(instructions):
		variables = {}
		for instruction in instructions:
			if instruction[0] == 'variable_assignment':
				variable_name = instruction[1]
				variable_value = instruction[2][1]
				if instruction[2][0] == 'var':
					variables[variable_name] = variables[variable_value]
				else:
					variables[variable_name] = variable_value
			if instruction[0] == 'store_line':
				variables[instruction[1]] = input("input:")
			if instruction[0] == 'print_line':
				variable_type = instruction[1][0]
				variable_value = instruction[1][1]
				if variable_type == "var":
					print(variables[variable_value])
				elif variable_type == "str":
					print(variable_value[1:-1])
				else:
					print(variable_value)
		print("STORED VARIABLES:", variables)