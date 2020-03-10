class SchoolMember:
	'''Represents any school member.'''

	def __init__(self,name,age):
		self.name = name
		self.age = age 
		print('(Initializes SchoolMember: {})'.format(self.name))


	def tell(self):
		"""Tell my details."""
		print('Name:"{}" Age:"{}"'.format(self.name, self.age),end="")


class Teacher(SchoolMember):
	'''Represents a student.'''

	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Initialized Student:{})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))


class Student(SchoolMember):
	'''Represents a Student'''

	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('Initialized Student:{}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))

class Rector(SchoolMember):

	def __init__(self,name,age,marks,gender):
		SchoolMember.__init__(self,name,age)
		self.marks = marks
		self.gender = gender
		print('Initialized Rector:{}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks:"{:d}" Gender:"{}"'.format(self.marks,self.gender))



t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
r = Rector('U Mya',59,1000,'Male')


print()


members =[t,s,r]
for member in members:
	member.tell()