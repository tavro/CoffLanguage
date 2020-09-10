# CoffLexer
Lexer for the Coff Language

Raw Text | Result
------------ | -------------
?@#[ | ("definition", "char")
. | ("end", "char")
+-\*/ | ("operator", "char")
0123456789 | ("number", "chars")
\><=();:]{},! | ("action", "char")
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_ | ("symbol", "chars")
any string | ("string", "chars")
anything else | ("undefined", "char/chars")
