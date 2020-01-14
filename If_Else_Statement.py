#If Else Staatements
If_Else_Statement.py

#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))



























Python conditions

Equals                                  -> x == y
Not Equals                              -> x != y
Less than                               -> x < y
Less than or equal                      -> x <= y
Greater than                            -> x > y
Greater or Equal                        -> x >= y
Boolean OR                              -> x or y, x | y
Boolean AND                             -> x and y, x & y
Boolean Not                             -> not x 


if -
else -

x = 10
>>> if x == 0:
...		print("x is zero")
... elif x != 0:
...		print("x is equal zero")
... elif x < 20:
... 	print("x is 20")
... elif x == 10:
... 	print("x is 10")
... else:
... 	print("x is nothing")
...

# If statement

x = 70
y = 60

if x < y:
	print("x is greater than y") 
elif x == y
	print("x and y are equal")

#Else

x = 50
y = 150
if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else:
	print("x is less than y")

# Short Hand If

if x < y: print("x is greater than y")

# Short Hand If ...Else

x = 50 
y = 150
print(x) if x > y else print(y)


#And is logical operator
x = 50 
y = 40
z = 100
if x > y and x > z:
	print("all conditions are True")
else:
	print("one condition is True")

# Or is logical operator

x = 50
y = 40
z = 100

if x > y or z < y:
	print("one of the conditions is True")
elif x > y and z > y:
	print("all conditions are True")
else:
	print("nothing else")

#Nested If is if  statement in if statements

x = 50

if x < 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
	else:
		print("No, x is not greater than 20")

else:
	print("x is 50")

#Pass Statement

x = 100
y = 50

if x > y:
	pass


------------------

int(input("Examination Result :"))
100 - 90     - A
90 - 70      - B
70 - 60      - C 
60 - 40      - D
40 - 10      - Fail

>>> Loops

if x >= 70 and x < 90:
	print("Grade B")
