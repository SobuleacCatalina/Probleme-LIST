"""
Se citesc elementele unei liste,din documentul input.txt, care reprezintă numere întregi (pozitive și negative). Să se afișeze la ecran:
	a) conținutul (elementele) listei /lista1
	b) lista sortată în ordine crescătoare / lista2
	c) lista sortată în ordine descrescătoare / lista3
	d) numărul de elemente din listă
	e) elementul MAX
	f) elementul MIN
	g) să se adauge la coadă în lista inițială elementul – 111. 
	Să se afișeze lista nou-formată. / lista4
	h) să se adauge pe poziția a doua din lista inițială elementul – 222. 
	Să se afișeze lista nou-formată. / lista5
"""
with open("input.txt","r") as f:
    x=map(int,f.readline())
    lista1=(list(x))
    print("lista initiala =",lista1)
    lista2=sorted(lista1)
    print("lista sortata crescator =",lista2)
    lista3=list(x)
    lista3.sort(reverse=True)
    print("lista sortata descrescator =",lista3)
    print("numarul de elemente din lista=",len(lista1))
    print("MAX =",max(lista1))
    print("MIN =",min(lista1))
    lista4=list(x)
    lista4.extend([111])
    print("lista nou formata cu adaugarea 111 =",lista4)
    lista5=list(x)
    lista5.insert(2,222)
    print("lista nou formata cu adaugarea 222 =",lista5)
