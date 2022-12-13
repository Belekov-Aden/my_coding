#1 Problem file my_modul.py
import my_module


#2 Problem 4 items add other list
from random import choice

names = ["Aibek", "Joomart", "Adinai", "Ermek",
         "Atai", "Aslan", "Lyazat", "Salavat",
         "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
new_n = []
for i in range(4):
    d = choice(names)
    new_n.append(d)

print(new_n)

#3 problem i do sys import for information about my CPU
import sys
from sys import platform

print(sys.platform)

#4 Problem
#Через терминал передайте Python несколько аргументов, а затем выведите их на экран.
#sys.stdin



#5 Problem
#create file in Desktop and in inside create random five files

import os
from random import choice

name = [
        "Aibek.jpg", "Joomart.mp4","Adinai.doc", "Ermek.docx",
        "Atai.tx", "Aslan.pdf", "Lyazat.zip", "Salavat.html",
        "Daniyar.psd", "Bolotbek.ai", "Alymbek.mp3", "Dastan.rar", "Maksat.png"
]

#os.mkdir('C:\\Users\Lenovo\Desktop\modulfiles')
#path = r'C:\Users\Lenovo\Desktop\modulfiles'
#os.path.isfile(path)

z = [

]

with open(r'C:\Users\Lenovo\Desktop\modulfiles', 'w') as cr:
        opens = cr.write
        for i in range(5):
                z.append(choice(name))
                opens(z)

