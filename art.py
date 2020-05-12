#!/usr/bin/python

#This Modules

from pyfiglet import Figlet



def render(text,style):
	f = Figlet(font=style)
	print('\n'*10)
	print(f.renderText(text))


render("webtester", 'Epic')
print("Code By Dyar Saadi")
