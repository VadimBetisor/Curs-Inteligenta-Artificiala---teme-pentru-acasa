#se da un vector cu n componente
#sa se calculeze suma componentelor lui
# produsul
# n>=1 n<=100
q=[]
i=0
s=0
p=1
n=int(input("Introduceti numarul de elementen = "))
if (n<1) or (n>100):
    print('Eroare - valoare inadmisibila')
else:
    while i!=n:
        a=str(input('Introduceti elementul = '))
        q.extend(a)
        i+=1
for element in q:
    s+=int(element)
    p*=int(element)
print('Suma elementelor vectorului=',s)
print('Produsul elementelor vectorului=',p)

