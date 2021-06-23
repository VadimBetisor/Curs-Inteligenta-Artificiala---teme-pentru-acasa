#se da un text sa se calculeze numarul
"""vocalelor special_characters = ""!@#$%^&*()-+?_=,<>/""
consoanelor 
simbolurilor care nu sunt litere
literelor mici
literelor mari
cifrelor"""
vocale=0
sp=0
consoane=0
cifre=0
mici=0
mari=0
import string
txt=str(input("Introduceti textul= "))
txtm=txt.lower()
vow=["a","o","u","e","i","A","O","U","E","I"]
spec=["!","@","#","$","%","^","&","*","(",")","-","+","?","_","=",",","<",">","/"]
cif=["0","1","2","3","4","5","6","7","8","9"]
for lit in txtm:
    if lit in vow:
        vocale+=1
    elif lit in spec:
        sp+=1
for lit1 in txt:
    if lit1 in string.ascii_uppercase:
        mari+=1
    if lit1 in string.ascii_lowercase:
        mici+=1
    if lit1 in cif:
        cifre+=1
for cs in txt:
    if (cs not in vow) and (cs not in spec) and (cs not in cif) :
        consoane+=1

    
    
print('Nr de vocale = ',vocale)
print('Nr de consoane = ',consoane)
print('Nr de caractere speciale = ',sp)
print('Nr de cifre = ',cifre)
print('Nr de litere mici = ',mici)
print('Nr de litere mari = ',mari)