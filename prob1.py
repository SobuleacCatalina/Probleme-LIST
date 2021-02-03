with open('input.txt','r') as f:
    nr=f.readline()
    n=[]
    n.extend(nr)
    li=map(int,n)
    cp=0
    cim=0
    for i in li:
        if i%2==0:
            cp+=1
        elif i==0:
            cp+=1
        else:
            cim+=1
with open('output.txt','w') as f:
    f.write(str(cp))
    f.write(" ")
    f.write(str(cim))