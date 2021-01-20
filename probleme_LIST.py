"""
Se citesc elementele unei liste, care reprezintă numere întregi (pozitive și negative). Să se afișeze la ecran:
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
lista1=[1,7,5,3,9,-4,-2,1,-5,9,7,5,13,-20]
print("lista initiala =",lista1)
lista2=sorted(lista1)
print("lista sortata crescator =",lista2)
lista3=[1,7,5,3,9,-4,-2,1,-5,9,7,5,13,-20]
lista3.sort(reverse=True)
print("lista sortata descrescator =",lista3)
print("numarul de elemente din lista=",len(lista1))
print("MAX =",max(lista1))
print("MIN =",min(lista1))
lista4=[1,7,5,3,9,-4,-2,1,-5,9,7,5,13,-20]
lista4.insert(len(lista1),111)
print("lista nou formata cu adaugarea 111 =",lista4)
lista5=[1,7,5,3,9,-4,-2,1,-5,9,7,5,13,-20]
lista5.insert(2,222)
print("lista nou formata cu adaugarea 222 =",lista5)