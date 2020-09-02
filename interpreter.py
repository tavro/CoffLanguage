class CoffProgram():
	def run_instructions(self, instructions):
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
			if instruction[0][0] == 'for_loop':
				for i in range(instruction[0][2][1], instruction[0][3][1]):
					self.run_instructions(instruction[1:])
			if instruction[0][0] == 'function':
				self.run_instructions(instruction[1:])
		#print("STORED VARIABLES:", variables)

	def pack_functions(self, instructions):
		packed_instructions = []
		function_template = []
		constructing_function = False
		for instruction in instructions:
			if constructing_function:
				if instruction == 'return_value':
					packed_instructions.append(function_template)
					function_template = []
					constructing_function = False
				else:
					function_template.append(instruction)
			else:
				if instruction[0] == 'function' or instruction[0] == 'for_loop':
					function_template.append(instruction)
					constructing_function = True
				else:
					packed_instructions.append(instruction)
		return packed_instructions