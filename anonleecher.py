#!/usr/bin/python3

#import googlesearch module using for searching
from googlesearch import search 
 
#getting info
print("What to search?")
a = input()

print("How many results?")
b = input()

#query to search 
tosearch = "site:anonfile.com " + a

for j in search(tosearch, tld="co.in", num=int(b), stop=int(b), pause=2): 
	print(j) 
