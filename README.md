# Coff Language
This project is something I am working on to learn/for fun.

coff.py is the entrypoint and does always go together with a program.coff file

to run your coff program simply write 
```
py coff.py
```
in  the terminal
## Example Programs

```
! Hello World in Coff

> "Hello World!"
```

```
! Simple program

# main
  @ i 0 10
    ? i == 10
      > "This is the last index, would you like to share some of your thoughts?"
      < answer
      > answer
    .
  .
.
```

## Variables

### String variables

variableName = "value"

### Int variables

variableName = 10

### Expression variables

variableName = 10+20+30/40\*50

### Variable variables

variableName = otherVariableName

## Loops

### For-loops

#### Alternative 1

@ variableName value1 value2

Loops variable from value1 up to value2

#### Alternative 2

@ value1 value2

Loops default variable called "i" from value1 up to value2

#### Alternative 3

@ endValue

Loops default variable called "i" from 0 up to endValue

## Conditions

### If-statement

? expression1 == expression2

## Functions

defining a function:

```
# functionName
	!do stuff
.
```

calling a function:

functionName

## Input

### Storing input in variables

< variableName

## Printing

### Printing strings

\> "Hello World"

Hello World

### Printing numbers

\> 42

42

### Printing expressions

\> 145+146-10\*20

91

### Printing variables

variableName = "value"

\> variableName

value

## Comments

### One-line comments

! This is a comment

## Goal

```
! Goal functionality and syntax

[PROGRAM]
	# main : variableName1, variableName2, variableName3
	  @ i 0 10
	    ? i == 10
	      > "This is the last index, would you like to share some of your thoughts?"
	      < answer
	      > answer
	    .
	  .
	.
.

program = PROGRAM
program.main : variable1, variable2, variable3
```
