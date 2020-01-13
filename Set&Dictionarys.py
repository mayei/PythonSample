#Sets

#includes a data type for sets.
#Curly braces or the set() function can be used to create sets.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)













                          #show that duplicates have been removed

'orange' in basket          
'crabgrass' in basket



        Demonstrate set operations on unique letters from two words

        a = set('abracadabra')
        b = set('alacazam')
        a                          # unique letters in a 
        a - b                      # Letter in a but not in b
        a | b                      # LLetter in a or b or both 
        a & b                      # Letters in both a and b
        a ^ b                      # Letter in a or b but not both

        a = { x for x in 'anracadabra' if x not in 'abc'}
        a



fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

fruits.add("cucumber")
fruits
fruits.update("grape")
fruits
fruits.remove("banana")
fruits
fruits.discard("kiwi")



>>>Dictionaries

#Dictionaries

#Another useful data type built into Python is the dictionary
tel = {'jack : 4098', 'sape': 4139}
tel['sape']
tel['guido'] = 4127
tel

del tel['sape']
tel['irv'] = 4137
tel

list(tel)  # Change to List

sorted(tel)  # Alphabet sorting

'guido'in tel

'sape' not in tel

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])  #Change to dict
dict(sape=4139, guido=4127, jack=4098)

{x: x**2 for x in (2, 4, 6)}

for  x in 2 2, 4, 6:
	print(x: x**2)
2 : 4
4 : 16
6 : 36	


{x: x**3 for x in (1, 2, 3, 4, 5)} 

1 : 1
2 : 8
3 : 27
4 : 64
5 : 125



#When loopinh through dictionaries

knights = {'gallahad' : 'the pure', 'robin' : 'the brave'}
for k, v in knights.items():
	print(k, v)


for i, v in enumerate(['tic', 'tac', 'toe']): 
	print(i, v)

for x, y in enumerate([1000, 2000, 3000]):
	print(x, y)



questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the hole grail', 'blue']
result = ['1', '2', '3']
for q, a, i in zip(questions, answers): 
	print('What is your {0}? It is {1}. It is No.{2}'.format(q, a, i)) 

print('{0} and {1}, {2} and {3}'. format ('spam', 'eggs', 'color', 'food'))

https//docs.python.org/3/tutorial/


>>> If_Else_statement