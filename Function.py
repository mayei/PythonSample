Function.py

def say_hello():
	print('Hello World')


say_hello()


#function_parametrer

def print_max(a,b):
	if a > b:
		print(a, 'is maximum')
	elif a == b:
		print(a,'is equal to', b)
	else:
		print(b, 'is maximum')

print_max(3,4)

x = 8
y = 11

print_max(x,y)

#local Variabnles

def func(x):
	print('x is',x)
	x = 2
	print('Changed local x to',x)

x = 50
func(x)
print('x is still', x)

x = 30

def func(x):
	x = 2

def funx(x)
	x = 10

func(x)
funx(x)
x
func(x) + funx(x)


#Global Statement

def func():
	global x

	print('x is',x)
	x = 2
	print('Changed global x to',x)

x = 50
func()
print('Value of x is',x)

x = 1
y = 2
global x = 10 y = 20

#Default Arguement Values in Functions

def say(,message, time=1):
	print(message * times)

say('Hello')
say('World', 5)
say('Good Bye')

#keyword Argument

def func(a, b=5, c=10):
	print('a is',a, 'and b is',b, 'and c is', c)


func(3, 8)
func(24, c=26)
func(c=29,a=39)

#VarArgs prarmeters
#function_VarArgs.py

def total(a=5, *numbers, **phonebook):
	print('a',a)

	for single_item in numbers:
		print('single_item',single_item)

	for first_part,second_part in phonebook.items():
		print(first_part,second_part)

total(10, 1, 2, 3,Jack=1123,John=2231,Inge=1459)
total(10, 1, 2, 3,12,15,33Jack=1123,John=2231,Inge=1459,Jame=2233)

#Return statement

def maximum(x, y):
if x > y:
	return x
elif x == y:
	retrn 'The numbers are equal'
else:
	return y

print(maximum(3,8))
print(maximum(20,10))

#DocString (Documentation Strings)
Function.py

def say_hello():
	print('Hello World')


say_hello()	


#function_parameter

def print_max(a,b):
	if a > b:
		print(a, 'is maximum')
	elif a == b:
		print(a,' is equal to', b)
	else:
		print(b,'is maximum')

print_max(3,4)		

x = 8
y = 11

print_max(x,y)


#Local Variables

def func(x):
	print('x is',x)
	x = 2
	print('Changed local x to',x)

x = 50
func(x)
print('x is still', x)	

x = 5

def func(x):
	x = 10
	print(x)


def funx(x)
	x = 20
	print(x)

x	
func(x)
funx(x)



#Global Statement

def func():
	global x 

	print('x is',x)
	x = 2
	print('Change global x to',x)

x = 50
func()
print('Value of x is',x )


#Default Argument Values in Functions

def say(message, times=1):
	print(message * times )

say('Hello')
say('World', 5 )	
say('Good Bye')


#Keyword Arugment

def func(a, b=5, c=10):
	print('a is',a,'and b is',b, 'and c is', c)

func(3, 8)
func(24, c=26)
func(c=29,a=39)


#VarArgs parameters
#function_VarArgs.py

def total(a=5, *numbers,  **phonebook):
	print('a',a)

	for single_item in numbers:
		print('single_item',single_item)

	for first_part,second_part in phonebook.items():
		print(first_part,second_part)

total(10, 1, 2, 3,Jack=1123,John=2231,Inge=1459)

#Return statement

def maximum(x, y)
	if x > y:
		return x
	elif x == y:
		return 'The numbers are equal'
	else:
		return y

print(maximum(3,8))	

print(maximum(20,10))		

#DocString (Documentation Strings)

def print_max(x, y):
	'''Prints the maximum of two numbers
		The Two values must be integers.
	'''

	x = int(x)
	y = int(y)

	if x > y :
		print(x, 'is maximum')

	elif x < y:
		print(y, 'is maximum')
	else:
		print(x,'&', y,'is equal')	

print_max(5,9)

print(print_max.__doc__)

def paper():
	'''1. There will be situations where your 
	program has to interact with the user. 
	For example, you would want to take input 
	from the user and then print some results 
	back. We can achieve this using the input()
	 function and print function respectively. '''

	 '''2. There will be situations where your 
	program has to interact with the user. 
	For example, you would want to take input 
	from the user and then print some results 
	back. We can achieve this using the input()
	 function and print function respectively. '''


print(paper.__doc__) 

doc.py



























def paper():
	'''1. There will be situations where your 
	program has to interact with the user.
	function and print function respectively.

	2. There will be situations where your 
	program has to interact with the user.
	function and print function respectively. '''


	print(paper.__doc__)




















