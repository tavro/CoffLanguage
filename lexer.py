from sly import Lexer
from sly import Parser

class CoffLexer(Lexer):
    tokens = {VARIABLE, NUMBER, STRING, PRINT, INPUT}
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    PRINT = r'>'
    INPUT = r'<'
    #FUNC = r'@'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'!.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def NEWLINE(self, t):
        self.lineno = t.value.count('\n')

class CoffParser(Parser):
    tokens = CoffLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
        )

    def __init__(self):
        self.env = { }

    @_('')
    def statement(self, p):
        pass

    @_('STRING')
    def expression(self, p):
        return ('str', p.STRING)

    @_('variable_assignment')
    def statement(self, p):
        return p.variable_assignment

    @_('print_line')
    def statement(self, p):
        return p.print_line

    @_('store_line')
    def statement(self, p):
        return p.store_line

    @_('expression')
    def statement(self, p):
        return (p.expression)

    @_('PRINT STRING')
    def print_line(self, p):
    	return ('print_line', p.STRING)

    @_('PRINT VARIABLE')
    def print_line(self, p):
    	return ('print_line', p.VARIABLE)

    @_('PRINT expression')
    def print_line(self, p):
    	return ('print_line', p.expression)

    @_('INPUT STRING')
    def store_line(self, p):
    	return ('store_line', p.STRING)

    @_('INPUT VARIABLE')
    def store_line(self, p):
    	return ('store_line', p.VARIABLE)

    @_('INPUT expression')
    def store_line(self, p):
    	return ('store_line', p.expression)

    @_('VARIABLE "=" expression')
    def variable_assignment(self, p):
        return ('variable_assignment', p.VARIABLE, p.expression)

    @_('VARIABLE "=" STRING')
    def variable_assignment(self, p):
        return ('variable_assignment', p.VARIABLE, p.STRING)

    @_('expression "+" expression')
    def expression(self, p):
        return ('add', p.expression0, p.expression1)

    @_('expression "-" expression')
    def expression(self, p):
        return ('sub', p.expression0, p.expression1)

    @_('expression "*" expression')
    def expression(self, p):
        return ('mul', p.expression0, p.expression1)

    @_('expression "/" expression')
    def expression(self, p):
        return ('div', p.expression0, p.expression1)

    @_('"-" expression %prec UMINUS')
    def expression(self, p):
        return p.expression

    @_('VARIABLE')
    def expression(self, p):
        return ('var', p.VARIABLE)

    @_('NUMBER')
    def expression(self, p):
        return ('num', p.NUMBER)

if __name__ == '__main__':
    lexer = CoffLexer()
    parser = CoffParser()
    env = {}

    with open("program.coff") as file:
    	for line in file:
        	tree = parser.parse(lexer.tokenize(line))
        	print(tree)