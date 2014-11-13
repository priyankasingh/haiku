import re
book = open('book.txt', 'r')

dictionary={}

booklist = []

with open('book.txt','r') as f:
    for line in f:
        for word in line.split():
           booklist.append(word.lower())

print len(booklist)

for i in range(len(booklist)):
	if booklist[i].isalpha() and booklist[i+1].isalpha() and i < len(booklist)-2:
		workingstring = booklist[i] +" "+ booklist[i+1]
		#print workingstring
		if workingstring not in dictionary:
			dictionary[workingstring]=[re.sub(r'\W+', '',booklist[i+2])]
		else:
			dictionary[workingstring].append(re.sub(r'\W+', '',booklist[i+2]))
		
print dictionary
		
		