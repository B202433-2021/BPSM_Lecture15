#!/usr/local/bin/python3

def questions():

	name = input("What is your name: ")
	age = int(input("What is your age: "))
	colour = input("What is your favourite colour: ")
	Python = input("Do you like Python: ")
	flat_earth = input("The Earth is flat, enter True or False: ")  

	return(name, age, colour, Python, flat_earth)

name, age, colour, Python, flat = questions()

user_info = {}

user_info["name"] = name
user_info["age"] = age
user_info["colour"] = colour
user_info["Python"] = Python
user_info["flat"] = flat

for k, v in user_info.items():
	print(k, v) 

if user_info["age"] < 50:
	print("You are young")
if user_info["colour"] != "Blue":
	print("Your favourite colour is wrong")
if user_info["flat"] == "True":
	print("You are silly.")

