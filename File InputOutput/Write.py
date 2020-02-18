# with open('test.txt', 'r') as rf:
# 	with open('Hello.txt','w') as wf:

# 		for line in rf:
# 			wf.write(line)

 with open('flower.jpg', 'rb') as rf:
 	with open('flower_copy.jpg', 'wb') as wf:

		for line in rf:
			wf.write(line)