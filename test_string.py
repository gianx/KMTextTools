#!/usr/bin/python
#coding=utf-8
#
# String function for Python
#

import sys

new_line = "\n"
not_words="\\|!\"£$%&/()=?^é*è+[]ç°§òàù@#¶;:_,.-<>".decode("utf-8")
out=""
mytext=u"""Ciao a tutti,
spero stiate bene!

Saluti,
Gian"""

class StringManager:
	def __init__ (self, original):
		self.text = original
		self.original = original

	def get_text(self):
		return self.text

	def get_original(self):
		return self.original
	
	def reset(self):
		self.text = self.original

	def capitalize(self):
		self.text = self.text.upper()

	def capitalize_single(self):
		self.text = self.text.title()
	
	def capitalize_first(self):
		self.text = self.text[0].upper() + self.text[1:len(self.text)]
	
	def lowercase(self):
		self.text = self.text.lower()

	def contrary(self):
		out = ""
		for x in range(0,len(self.text)):
			out += self.text[len(self.text)-x-1]
		self.text = out

	def contrary_byline(self):
		out = ""
		for y in self.text.split(new_line):
			for x in range(0,len(y)):
				out += y[len(y)-x-1]
			out += new_line
		self.text = out
	
	def reverse_lines(self):
		self.text = "\n".join(self.text.split(new_line)[::-1])

	def count_lines(self):
		return len(self.text.split(new_line))

	def count_words(self):
		count = 0
		for x in self.text.split(new_line):
			for y in x.split(" "):
				if y not in not_words:
					count += 1
		return count

#
# START MAIN
#
if len(sys.argv)<3:
		print "ERROR: Syntax: [COMMAND] [TEXT]"
		sys.exit()
print sys.argv
command=sys.argv[1]
mytext=sys.argv[2]

mystr=StringManager(mytext)
if command.lower()=="reset": mystr.reset()
if command.lower()=="Capitalize all text": mystr.capitalize()
if command.lower()=="Capitalize only first letter": mystr.capitalize_first()
if command.lower()=="Capitalize every first letter": mystr.capitalize_single()
if command.lower()=="Lowercase": mystr.lowercase()
if command.lower()=="Contrary": mystr.contrary()
if command.lower()=="Contrary by line": mystr.contrary_byline()
if command.lower()=="Reverse lines": mystr.reverse_lines()
if command.lower()=="Count lines": out = mystr.count_lines()
if command.lower()=="Count words": out = mystr.count_words()
if (mystr.get_text() != mystr.get_original()) or (command.lower()=="reset"):
	out=mystr.get_text()
print out
#print command.lower()
