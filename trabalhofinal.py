#Crie a partir da classe Conta, contas filhos ContaSalário, ContaEspecial,
#ContaPoupança. Definir métodos saque(), levando em consideração o saldo ou o limite
#para contas especiais. Implementar atributos e métodos que achares necessário.
#Implementar o método __main__ para incluir, alterar e excluir objetos destas contas, e
#ainda, chamada dos seus métodos específico.
#Utilizar o máximos dos conceitos vistos nas aulas anteriores.

#Caroline Caprini da Silveira - https://github.com/cprnn

def main():
    menu = 0

    while opt != "9":
        print("Acesse a conta:")
        print("1: Conta salário")
        print("2: Conta especial")
        print("3: Conta poupança")
        print("9: Sair")
        opt = input("Selecione:\n")