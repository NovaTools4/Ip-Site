import random

from random import *

from cfonts import render

from time import sleep

import os 

import socket as sock

F = '\033[2;32m'

Z = '\033[1;31m'

X = '\033[1;33m' 

F = '\033[2;32m'

A = '\033[2;34m'

C = '\033[2;35m' 

B = '\033[2;36m'

Y = '\033[1;34m' 

G = ['red','green','blue']

v = str(choice(G))

b = str(choice(G))

k = str(choice(G))

bn = render('NOVA',colors=[v, b, k],align='center')

ar = render('IP',colors=[v, b, k],align='center')

def vb():

	bn = render('NOVA',colors=[v, b, k],align='center')
  ar = render('IP',colors=[v, b, k],align='center')

	for bn in bn.splitlines():

		sleep(0.10)

		print(bn)

	os.system('clear')

	for ar in ar.splitlines():

		sleep(0.10)

		print(ar)

vb()

		

try:

 print("\n")

 print("Tool By The Jordan Ghost")

 print("@VZX_TEAM                        @C0_28")

 print()

 url = input(F+"Enter Url : ")

 if "://" in url:

 	print()

 	print(C+"Please Delete :// or http or https From Url")

 	print()

 if "://" not in url:

 	ip = sock.gethostbyname(url)

 	print()

 	print(Y+f"Url : {url}")

 	print(Y+f"Ip : {ip}")

 	print()

 else:

 	ip = sock.gethostbyname(url)

 	print()

 	print(Y+f"Url : {url}")

 	print(Y+f"Ip : {ip}")

 	print()

except:

 print(f"{C}Error, Please Try Agin ...")
