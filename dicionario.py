#Crie um programa que cadastre informações de várias pessoas
#(nome, idade e cpf) e depois coloque em um dicionário. Depois
#remova todas as pessoas menores de 18 anos do dicionário e
#coloque em outro dicionário. 

info = {}
aux = 1
opt = 0
age = 18

def intInput(inputData):
    data = None
    while data is None:
        data = input(inputData)
        try:
            data = int(data)
        except:
            data = None

    return data

def getUnderAge(dict):
    dictMin = {}
    for cont, value in dict.items():
        if(value["idade"] < age):
            dictMin[cont] = value

    for cont in dictMin:
        dict.pop(cont)

    return dictMin

while aux != 0:
    opt = int(input('Digite 1 para inserir um novo contato, 2 para acessar a lista de usuários menores de 18 anos e 0 para sair:'))
    
    if(opt == 1):
        info[intInput("CPF: ")] = {
        "nome": input("Nome: "),
        "idade": intInput("Idade: ")
        }
    elif(opt == 2):
        minor = getUnderAge(info)
        print(minor)
    elif(opt == 0):
        aux = 0
    else:
        print("Erro, repita novamente")


print(info)

