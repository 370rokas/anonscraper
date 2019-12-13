#!/usr/bin/python3
	
import requests
from bs4 import BeautifulSoup
import re

print("What to search?")
a = input()

query = a.replace(' ', '+')
link = "https://www.google.com/search?&q=site%3Aanonfile.com+" + query #thanks to Apoc for giving me that syntax

response = requests.get(link)

returnedtext = response.text

#url finder

urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', returnedtext) #thanks to Drizzy for the regex

for x in range(len(urls)):
	if "anonfile.com" in urls[x]:
		if urls[x] != "https://anonfile.com":
			if not "google." in urls[x]:
				print(urls[x]) 
