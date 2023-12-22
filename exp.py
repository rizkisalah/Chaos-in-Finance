import numpy as np
def explyap(serie,m,q,epsilon):
    T=len(serie)
    t1=np.random.randint(20,620)
    d1=abs(serie[t1]-serie[1])
    d2=abs(serie[t1+q]-serie[1+q])
    g=d2/d1
    sum=np.log(g)
    exp=0
    for k in range (2,int((T*m-1)/q)):
        a=k
        for j in range (int(T/2)):
            if abs(serie[j]-serie[1+q])<epsilon and abs(serie[j]-serie[1+q])!=0:
                k=j
                break
            else :
                j+=1
        d1=abs(serie[k]-serie[1+(k-1)*q])
        d2=abs(serie[k+q]-serie[1+k*q])
        g=d2/d1
        sum+=np.log(g)
        k=a
        k+=1
    exp=sum/(T*m - 1)
    return exp


