fibo = []
fibo.append(0)
fibo.append(1)

def intInput(inputData):
    aux = None
    while aux is None:
        aux = input(inputData)
        try:
            aux = int(aux)
        except:
            aux = None

    return aux

tam = intInput("Digite o tamanho da serie(N):")

while len(fibo) < tam+1:
	aux = len(fibo)
	fibo.append(fibo[aux-1] + fibo[aux-2])

print(fibo)

