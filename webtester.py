#!/usr/bin/python

import art
import socket
import os
import requests


def menu():
	print("[1-] Scanning By Site Url :")
	print("[2-] Get IP By Url : ")
	menu_input = int(input("Please Choose Our Options By Type a Number : "))
	if  menu_input==1:
		burl()
	elif menu_input==2:
		geti()
	else:
		print("Error")



def burl():
	target_url = input("Url Target is : ")
	response = requests.get(target_url)
	if response.status_code==200:
		print("===============")
		print("Your Site is Up")
		print("===============")
	elif response.status_code==404:
		print("====================")
		print("Your Site Down Sorry")
		print("====================")
	


def geti():
	target_2 = input("Your Target :")
	print(socket.gethostbyname(target_2))
	fh = open("IP.txt", "w")
	fh.write(socket.gethostbyname(target_2))
	fh.close()



if __name__ == "__main__":
	menu()
