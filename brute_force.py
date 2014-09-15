#-*- coding: utf-8 -*-
#generates random character strings from ascii tab and compares with the typed one
import time
import md5

Word = input("type word: ")
numerlicznika = 1
ciagliter =""
start = time.time()
#base------------------

alpha= ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó", "p", "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż",]


#Recurency function----
def Rec(ciagliter, numerlicznika, alpha, Word):
	u"""Creates ALL character strings from alpha and compares with the typed word"""
	if numerlicznika<=0:
		b = md5.new(ciagliter).hexdigest()
		if b == Word:
			print "to jest to: " +ciagliter
			return -1
		else: 
			return 0

	for i in range(34):
		if Rec(ciagliter+alpha[i], numerlicznika-1, alpha, Word)==-1:
			return -1
	return 0
	
def Rec2(ciagliter,alpha, Word):
	for numerlicznika in range(30):
		a = Rec(ciagliter, numerlicznika, alpha, Word)
		if a == -1:
			return -1
	return 0
		
#Rec call--------------		
if __name__ == "__main__":
	Rec2(ciagliter, alpha, Word)

#Ending----------------
end = time.time()
Time = end - start
print Time

