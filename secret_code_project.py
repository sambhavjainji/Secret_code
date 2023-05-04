#WAP TO TRANSLATE A MESSAGE INTO SECRET CODE LANGUAGE.
n=input()
l=[]
w=n.split(" ")
print(w)
for i in w:
    if(len(i)<3):
        p=i[::-1]
        l.append(p)
    else:
        r1="rdf"
        r2="fdv"
        s=r1+i[1:]+i[0]+r2
        l.append(s)

k=""
for j in l:
    k=k+" "+j
print(k)


"""n=input()
l=[]
w=n.split(" ")
print(w)
for i in w:
    if(len(i)<3):
        p=i[::-1]
        l.append(p)
    else:
        
        s=i[-4]+i[3:-4]
        l.append(s)

k=""
for j in l:
    k=k+" "+j
print(k)  """
