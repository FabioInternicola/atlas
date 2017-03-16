import os
import sys
import wikipedia



namef=open('name','r')
name = namef.read()
namef.close()

if name=="":
	print("Before using this program, you have to contuine with the installation.\n")
	raw_input('Press SEND.')
	os.system("python setup.py")
	sys.exit()

def clear():
	os.system("clear")
	print("------------------------------------------\n")

clear()

def start():
	x=0

	while x==0:
		clear()
		print("Hello, %s. How can I help you ?\n" % name)
		prompt2=raw_input("")
		if prompt2=="search":
			search()

def end():
	sys.exit()

def search():
	string_searched=raw_input("What do you want to search ?\nsearch ")
	print wikipedia.summary(string_searched)


i=0
while i==0:
	prompt=raw_input("")
	if prompt=="start":
		start()
	if prompt=="end":
		end()
	if prompt=="exit":
		end()