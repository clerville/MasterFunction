from random import *
import string


#kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon
Alfab=string.ascii_letters
Alfanb=randint(6,8)
password=""
for i in range(Alfanb):
    let=randint(0,25)
    if Alfab[let] in password:
        Alfanb= randint(6,8)
    else:
        password+=Alfab[Alfanb]
print(password)