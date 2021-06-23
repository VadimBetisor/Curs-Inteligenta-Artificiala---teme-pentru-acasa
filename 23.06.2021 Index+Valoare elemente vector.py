#print out all elements with even index and odd value
n=int(input("Introduceti n = "))
i=0
w=0
q=[]
r=n
while i!=n:
        a=str(input('Introduceti valoarea elementului = '))
        q.append(a)
        i+=1
print(q)
while w!=r:
    w+=1
    if (w%2==0) and (w!=0):
        if (int((q[w])))%2!=0:
            print(q[w])
