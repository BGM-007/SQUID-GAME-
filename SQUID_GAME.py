import random as r
s=0
b=0
l=["BGM",'KESH','HEMANAADHAN','KISHORE A','KISHORE N']
while s==0:
    print(l[b])
    print('\n\t\t\t',r.randint(0,100)*2)
    s=int(input('\n\t\t\t\t\tGive status : \n\t\t\t\t\t'))
    if b < len(l)-1:
        print(b)
        b+=1
    else:
        b=0
    