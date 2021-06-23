#create a victorina that will ask the user how much is 
#2+2 until it answers right.
n=int(input('Cât face 2 + 2 = '))
a=True
while a:
    if n==4:
        print(
'CORECT. BRAVO!!!'
    )
        a=False
        break
    else:
        n=int(input('GREȘIT. Cât face 2 + 2 = '))
        a=True

