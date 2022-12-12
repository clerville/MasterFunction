#Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè.

import string
Afm = input("insert your words ::")
endeks=[]
for i in Afm:
    endeks.append(str(string.ascii_lowercase.index(i)))
print("-" .join(endeks))