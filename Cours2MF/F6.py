#Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè.

import string
from random import*
Alfab=string.ascii_letters

num=input("index io::")
word=[]
for i in num.split("-"):
   word.append(Alfab[int(i)])
print("".join(word))

