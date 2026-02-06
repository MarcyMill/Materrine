# Materrine™ - Database for everyone. 
# WHAT YOU SEE IS WHAT YOU GET. 

#Marcy Mill
################################################
# Codes. 

# Packages. 

import time
import random
import shelve
import os
import numpy as np
import sys
import getpass

# Classes. 

class MaterrineInfoError(Exception):
	pass

class MaterrineTypeError(Exception):
	pass

class MaterrineLenghtError(Exception):
	pass

class MaterrineMatchError(Exception):
	pass

class MaterrineSurpriseNotAnError(Exception):
	pass

class MaterrineOwnershipError(Exception):
	pass

class MaterrineNameError(Exception):
	pass

# Values. 

d1 = np.zeros((120, 120), dtype=object)
d2 = np.zeros((120, 120), dtype=object)
d3 = np.zeros((120, 120), dtype=object)
d4 = np.zeros((120, 120), dtype=object)
d5 = np.zeros((120, 120), dtype=object)
d6 = np.zeros((120, 120), dtype=object)
d7 = np.zeros((120, 120), dtype=object)
d8 = np.zeros((120, 120), dtype=object)
d9 = np.zeros((120, 120), dtype=object)
d10 = np.zeros((120, 120), dtype=object)

users = []
passwords = []

# Colour codes. 

fg_colors = {
	"black": "\033[90m",
	"red": "\033[91m",
	"green": "\033[92m",
	"yellow": "\033[93m",
	"blue": "\033[94m",
	"magenta": "\033[95m",
	"cyan": "\033[96m",
	"white": "\033[97m"
}

bg_colors = {
	"black": "\033[100m",
	"red": "\033[101m",
	"green": "\033[102m",
	"yellow": "\033[103m",
	"blue": "\033[104m",
	"magenta": "\033[105m",
	"cyan": "\033[106m",
	"white": "\033[107m"
}

# Colouring function. 
def colour(text, fg="white", bold=False, bg=None):
	prefix = ""
	if bold:
		prefix += "\033[1m"
	prefix += fg_colors.get(fg.lower(), "\033[97m")
	if bg:
		prefix += bg_colors.get(bg.lower(), "")
	return f"{prefix}{text}\033[0m"

# Core database functions. 
storage_path = os.path.join(os.path.dirname(__file__), "data.db")

def load_data():
	with shelve.open(storage_path) as db:
		d1 = db.get("d1", np.zeros((120, 120), dtype=object))
		d2 = db.get("d2", np.zeros((120, 120), dtype=object))
		d3 = db.get("d3", np.zeros((120, 120), dtype=object))
		d4 = db.get("d4", np.zeros((120, 120), dtype=object))
		d5 = db.get("d5", np.zeros((120, 120), dtype=object))
		d6 = db.get("d6", np.zeros((120, 120), dtype=object))
		d7 = db.get("d7", np.zeros((120, 120), dtype=object))
		d8 = db.get("d8", np.zeros((120, 120), dtype=object))
		d9 = db.get("d9", np.zeros((120, 120), dtype=object))
		d10 = db.get("d10", np.zeros((120, 120), dtype=object))
		users = db.get("users", [])
		passwords = db.get("passwords", [])
	return d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords




def save_data(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords):
	with shelve.open(storage_path, "c") as db:
		db["d1"] = d1
		db["d2"] = d2
		db["d3"] = d3
		db["d4"] = d4
		db["d5"] = d5
		db["d6"] = d6
		db["d7"] = d7
		db["d8"] = d8
		db["d9"] = d9
		db["d10"] = d10
		db["users"] = users
		db["passwords"] = passwords


d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords = load_data()

# Tools functions. 

def login(username=None, pwd=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if username is None or pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
		if passwords[users.index(username)] == pwd:
			print(f"Welcome back, {username}! ")
			return True
		else:
			raise MaterrineInfoError("Username or password invalid. ")
	else:
		if passwords[users.index(username)] == pwd:
			return True
		else:
			raise MaterrineInfoError("Username or password invalid. ")			

def register(name=None, password=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if name is None or password is None:
		name = input("Enter your new username here:    ")
		password = getpass.getpass("Enter your new password here:    ")
		rpassword = getpass.getpass("Enter your new password here again:    ")
	rpassword = password
	if password != rpassword:
		raise MaterrineInfoError("Username or password invalid. ")
	if name not in users:
		users.append(str(name))
		passwords.append(str(password))
		save_data(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords)
		return True
	else:
		raise MaterrineNameError(f"Username '{name}' is existed. ")


def store(tar, ct, whom1=None, password1=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if type(ct) != list:
		raise MaterrineTypeError("Element 'tags' must be a list. ")
	if len(ct) > 117:
		raise MaterrineLengthError("Length of element 'tags' must be ≤117. Perhaps you can store other data in another database which has the same name as this one. ")
	if password1 is None and whom1 is None:
		whom1 = input("Registered name:    ")
		password1 = getpass.getpass(f"Password for {whom1}:    ")
			
	pl = []
	if passwords[users.index(whom1)] == password1:
		preparedList = []
		for i in range(120):
			preparedList.append(0)
		preparedList[0] = whom1
		preparedList[1] = tar
		for i in range(len(ct)):
			preparedList[i + 2] = ct[i]
		preparedList[len(ct) + 3] = "END"
		pos = np.argwhere(d1 == whom1)
		for i in range(len(pos)):
			if pos[i][0] == 0:
				pl.append(i)
		p = []
		for i in range(len(pl)):
			if d1[pl[i]][1] != 0:
				p.append("NotFound")
			else:
				d1[pl[i]][1] = tar
				for j in range(len(ct)):
					d1[pl[i]][j + 2] = ct[j]
				d1[pl[i]][len(ct) + 2] = "END"
				save_data(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords)
				return d1[pl[i]]
		if len(p) == len(pl):
			d1 = np.vstack((d1, preparedList))
			save_data(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords)
			return d1[len(d1) - 1]
	else:
		raise MaterrineInfoError("Username or password invalid. ")		

			
		
def view_all(pwd):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if pwd == passwords[0]:
		return users, passwords, d1

def view_database(pwd):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if pwd == passwords[0]:
		return d1

def view_users(pwd):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if pwd == passwords[0]:
		return users


			
def view_pwd(pwd):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if pwd == passwords[0]:
		return passwords

def clear(pwd):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if pwd == passwords[0]:
		d1 = np.zeros((120, 120), dtype=object)
		d2 = np.zeros((120, 120), dtype=object)
		d3 = np.zeros((120, 120), dtype=object)
		d4 = np.zeros((120, 120), dtype=object)
		d5 = np.zeros((120, 120), dtype=object)
		d6 = np.zeros((120, 120), dtype=object)
		d7 = np.zeros((120, 120), dtype=object)
		d8 = np.zeros((120, 120), dtype=object)
		d9 = np.zeros((120, 120), dtype=object)
		d10 = np.zeros((120, 120), dtype=object)


		users = users[1:len(users)]
		passwords = passwords[1:len(passwords)]
		save_data(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords)
		return True
	


def is_pos(num):
	if num != 0 and num == abs(num):
		return True
	else:
		return False

def is_valid(line, pos):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	endpos = max(i for i, v in enumerate(line) if v == "END")
	if pos < endpos and is_pos(pos):
		return True
	else:
		return False

def is_dups(l):
	workable = []
	for i in l:
		if i in workable:
			return False
		else:
			workable.append(i)
	return True

def nodups(l):
	outputs = []
	for i in l:
		if i in outputs:
			continue
		else:
			outputs.append(i)
	return outputs
	

def search(tar, username=None, pwd=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if username is None or pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
	outputs = []
	main = []
	cons = []
	if passwords[users.index(username)] == pwd:
		userbase = mine(username, pwd)
		for i in userbase:
			for j, k in enumerate(i):
				if k == tar and j != 0 and is_valid(i, j):
					if j == 1:
						cons.extend(i[2:])
					else:
						main.append(i[1])
		main = nodups(main)
		outputs.append(main)
		outputs.append(cons)
		return outputs
	else:
		raise MaterrineInfoError("Username or password invalid. ")

def tags(tar, username=None, pwd=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if username is None or pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
	o = search(tar, username, pwd)
	return o[1]

def data(tar, username=None, pwd=None): 
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if username is None or pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
	o = search(tar, username, pwd)
	return o[0]
		
def mine(username=None, pwd=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	userbase = []
	if username is None and pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
	if passwords[users.index(username)] == pwd:
		for j, k in enumerate(d1):
			if k[0] == username:
				userbase.append(k)
		return userbase
	else:
		raise MaterrineInfoError("Username or password invalid. ")
		
def view(pos, username=None, pwd=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if type(pos) != list:
		raise MaterrineTypeError("Element 'pos' must be a list. ")
	if username is None or pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
	if passwords[users.index(username)] == pwd and d1[pos[0]][0] == username and is_valid(d1[pos[0]], pos[1]):
		return d1[pos[0]][pos[1]]
	else:
		raise MaterrineInfoError("Username or password or position invalid. ")
		
def delete(pos, username=None, pwd=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if type(pos) != list:
		raise MaterrineTypeError("Element 'pos' must be a list. ")
	if username is None or pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
	if passwords[users.index(username)] == pwd:
		if d1[pos[0]][0] == username and is_valid(d1[pos[0]], pos[1]):
			d1[pos[0]][pos[1]] = 0
			bp = max(i for i, v in enumerate(d1[pos[0]]) if v == "END")
			d1[pos[0]][bp] = 0
			d1[pos[0]][bp - 1] = "END"
			save_data(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords)
			return True
		else:
			raise MaterrineOwnershipError("The place where you wanted to delete is not yours. ")
	else:
			raise MaterrineInfoError("Username or password invalid. ")
		
			
def fill(pos, fillby, username=None, pwd=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if type(pos) != list:
		raise MaterrineTypeError("Element 'pos' must be a list. ")
	if username is None or pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
	if passwords[users.index(username)] == pwd and d1[pos[0]][0] == username and is_valid(d1[pos[0]], pos[1]):
		d1[pos[0]][pos[1]] = fillby
		save_data(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords)
		return True
	else:
		raise MaterrineInfoError("Username or password invalid. ")

def jfill(line, tar, fillby, username=None, pwd=None):
	if username is None or pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
	if passwords[users.index(username)] == pwd and d1[line][0] == username and tar in d1[line]:
		outputs = []
		for i, v in enumerate(d1[line]):
			if v == tar and is_valid(d1[line], i):
				outputs.append(fillby)
			else:
				outputs.append(v)
		d1[line] == outputs
		save_data(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords)
		return True
	else:
		raise MaterrineInfoError("Username or password invalid. ")

def line(line, username=None, pwd=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if username is None or pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
	if passwords[users.index(username)] == pwd and d1[line][0] == username:
		return d1[line]
	else:
		raise MaterrineInfoError("Username or password or position invalid. ")


def get(tar, username=None, pwd=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if username is None or pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
	if passwords[users.index(username)] == pwd:
		userbase = [i for i, v in enumerate(d1) if v[0] == username]
		allpos = []
		for i in userbase:
			if tar in d1[i].tolist():
				poshere = [j for j, k in enumerate(d1[i]) if k == tar and is_valid(d1[i], j)]
				allpos.append(i)
				allpos.append(poshere)
		return allpos
	else:
		raise MaterrineInfoError("Username or password invalid. ")

# Edit user informations. 

def change_password(username=None, pwd=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if username is None or pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your old password here:    ")
	pwd = str(pwd)
	if passwords[users.index(username)] == pwd:
		newpass = getpass.getpass("Enter your new password here:    ")
		newpasstwice = getpass.getpass("Enter your new password again:    ")
		if newpass == newpasstwice:
			passwords[user.index(username)] == newpass
			save_data(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords)
			return True
		else:
			raise MaterrineMatchError("Passwords not matched. ")
	else:
		raise MaterrineInfoError("Username or password invalid. ")
			
def change_username(username=None, pwd=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if username is None or pwd is None:
		username = input("Enter your old username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
	if passwords[users.index(username)] == pwd:
		nn = input("Enter your new username:    ")
		if nn in users:
			raise MaterrineNameError(f"Name '{nn}' is existed. ")
		else:
			users[users.index(username)] = nn
			save_data(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords)
			return True
	else:
		raise MaterrineInfoError("Username or password invalid. ")
			

# Surprise function room() ! 
def room(k):
	if k == "Materrine™" or k == "Marcy is me" or k == "M":
		raise MaterrineSurpriseNotAnError("Suprise! You just found the secret function room() ! This is the reward for the people who read my codes!")


def total(username=None, pwd=None):
	global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, users, passwords
	if username is None or pwd is None:
		username = input("Enter your username here:    ")
		pwd = getpass.getpass("Enter your password here:    ")
	if passwords[users.index(username)] == pwd:
		return len(mine(username, pwd))
	else:
		raise MaterrineInfoError("Username or password invalid. ")
		
# Infos functions. 

def license():
	mit = """
	MIT License

	Copyright (c) 2026 MarcyMill
	
	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:
	
	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.
	
	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.
	"""
	print(colour(mit, "green", bold = True, bg = None))
	
def author():
	authorinfo = """
	Marcy Mill is the author of Materrine™. He wrote Materrine™ alone in his study at home. He is a man which is attracted by the beauty of maths and by the beuaty of programming. He loves everything in this universe which is logical. His motto is "The process is the reward.". Visit his Github account which is barely nothing => MarcyMill. Anything you wants to say to him or maybe the improvements of Materrine™ you wants to share with him can be sent to his email address:
	marcy@marphire.com. And he has another Python package called MarStar, which is an ultimate game platform. He even gots his own website marphire.com, but not fully finished.
	You can ask @MarcyMill to help you with designing projects, he's boring. Marock™, Marphire™... is all his projects. 
	"""
	print(colour(authorinfo, "cyan", bold = True, bg = None))

def help():
	txt1 = """




	
		Materrine™ - Database for everyone. 
									By Marcy


		|Manuals for Materrine™, MaterrineBase™, MaterrineMe™ and MaterrineMine™. |


		-------------------------------------------------------------------------------------------------------------------------
		Hint: all the functions below can add elements username and password behind to skip the user verifications. E. g. search(obj, YourUsername, YourPassword) aplied on every function. 
		
	
		register(): To register an account.
		
		store(target, tags): To store data into MaterrineBase™, tags are the things related to target, in the format of a list. 
		
		search(obj): Search obj in your own database, will be outputs as this two-demensional-list-format below:
			[[mainData1, mainData2...], 
			 [tags1, tags2...]
			] .

		mine(): Which allows you to view your MaterrineMine™ - your own database. 

		delete(position): Delete the object on that position you mentioned. 

		fill(position, fillby): To fill the object in that position you mentioned by fillby. 

		help(): Here your are! To view our MaterrineUniversalManual™. 

		license(): To read our MIT license.

		author(): To know better of Materrine™ 's author Marcy Mill.

		change_password(): To change your password for your account. 

		jfill(line, target, fillby): To fill every targets you mentioned in the function in line by fillby. 

		login(): To view your infos. So-called 'MaterrineMe™'. 

		get(tar): Get the postion of tar. 

		view(pos): View specific position. 

		line(line): View specific row. 

		tags(tar): To view all the tags related to tar. 

		data(tar): To view all the data related to tar. 

		total(): To get the quantities of your database(s) . 

		|WHAT YOU SEE IS WHAT YOU GET|
		
	"""
	print(colour(txt1, "green", bold = True, bg = None))