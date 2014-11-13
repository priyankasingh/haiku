import re
book = open('book.txt', 'r')

dictionary={}

booklist = []

with open('book.txt','r') as f:
    for line in f:
        for word in line.split():
           booklist.append(re.sub(r'\W+', '', word))  

print len(booklist)

for i in range(len(booklist)):
	if i < len(booklist)-1 and booklist[i].lower() not in dictionary:
		dictionary[booklist[i].lower()]=[booklist[i+1].lower()]
	elif i < len(booklist)-1:
		dictionary[booklist[i].lower()].append(booklist[i+1].lower())
		
print dictionary
		
		