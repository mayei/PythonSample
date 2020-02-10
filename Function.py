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
