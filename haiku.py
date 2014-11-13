import re
book = open('book.txt', 'r')

dictionary={}

booklist = []

with open('book.txt','r') as f:
    for line in f:
        for word in line.split():
           booklist.append(word)

print len(booklist)

for i in range(len(booklist)):
	if booklist[i].isalpha():
		if i < len(booklist)-1 and booklist[i].lower() not in dictionary:
			dictionary[booklist[i].lower()]=[re.sub(r'\W+', '',booklist[i+1].lower())]
		elif i < len(booklist)-1:
			dictionary[booklist[i].lower()].append(re.sub(r'\W+', '',booklist[i+1].lower()))
		
print dictionary
		
		