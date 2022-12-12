from random import *
import string


#kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.

Alfanum=string.ascii_letters+string.digits
nomb = randint(6,8)
password=""
for i in range (nomb):
    indice=randint(0,61)
    if Alfanum[indice] in password:
          indice=randint(0,61)
    else:
        password+=Alfanum[indice]  
print(password)   