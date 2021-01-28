with open("input.txt","r") as f:
    prenume=f.readline()
    varsta=f.readline()
for i in range(0,len(prenume)):
    for j in range(0,len(varsta)):
        print(prenume[i],"are varsta de",varsta[j],"ani")
prenume.extend(["Andreea","Ioan"])
varsta.extend([34,23])
prenume.remove("Ana")
varsta.pop(prenume.index("Ana"))
print(prenume[0:3])