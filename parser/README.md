# CoffParser
Parser for the Coff Language

Object | Characteristics
------------ | -------------
Program | vector(Instruction)
Class | Symbol, vector(Symbol), vector(Instruction)
Function | Symbol, vector(Symbol), vector(Instruction)
Loop | Symbol, Number, Number, vector(Instruction)
Variable | Symbol, String/Number
Operation | Operator, Number/Variable/Operation, Number/Variable/Operation
Assignment | Symbol, Variable/String/Number/Operation
Condition | ConditionType, String/Number/Variable/Operation/Condition, String/Number/Variable/Operation/Condition, vector(Instruction)
Print | String/Number/Variable/Operation
Input | String/Number/Variable/Operation
Instruction | Class/Function/Loop/Variable/Operation/Condition/Assignment/Print/Input

