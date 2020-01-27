# fibonacci.py

# Fibonacci nubers module

# n = int(input('please enter a number: '))

def fib(n): #wrote fibonacci series up to n
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()
# a = 0
# b = 1
# a = b
# b = a + b

# Go to fibonacci powerpoint

def fib2(n):  # return fibonacci series up to n
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

def name():
	print("Hello World")

def hello():
	print(1, 2, 3, 4, 5)


		# >>> fib # import
