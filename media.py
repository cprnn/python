def media(list):
	soma = 0
	
	for el in list:
		soma += el

	return soma/len(list)

def intInput(inputData):
    data = None
    while data is None:
        data = input(inputData)
        try:
            data = int(data)
        except:
            data = None

    return data

lista = []
elements = intInput("Digite o numero de elementos da lista: ")

for i in range(elements):
	lista.append(intInput("Valor("+str(i+1)+"): "))

print("Media aritimetica dos elementos da lista: "+str(media(lista)))
