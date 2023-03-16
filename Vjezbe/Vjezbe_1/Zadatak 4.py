def funkcija(t1,t2):
    x1,y1=t1
    x2,y2=t2
    if not t1==t2:
        k=(y2 - y1)/(x2 - x1)
        n=-k*x1+y1
        if n<0:
            y= str(k)+'x'+str(n)
            print(y)
        if n>0:
            y=str(k)+'x'+'+'+str(n)
            print(y)
        if n==0:
            y=str(k)+'x'
            print(y)
    else:
        print('Unijeli ste koordinate istih točaka, unesite ponovno.')
funkcija((2,2),(5,5))