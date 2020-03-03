

class ShortInputException(Exception):
	'''A user-defined exception class.'''

	def __int__(self, length,atleast):
		Exception.__int__(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something-->')
	if len(text) < 3:
		raise ShortInputException(len(text), 3)
		#Other work can contiune as usual here

except EOFError:
	print('Why did you dod an EOF on me?')

except ShortInputException as ex:
	print(('ShortInputException: The input was ' + '{0} long, edpected at least{1}')
	.fornmat(ex.length, ex.atleast))
else:
	print('No exception was raised.')