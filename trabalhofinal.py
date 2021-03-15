#Crie a partir da classe Conta, contas filhos ContaSalário, ContaEspecial,
#ContaPoupança. Definir métodos saque(), levando em consideração o saldo ou o limite
#para contas especiais. Implementar atributos e métodos que achares necessário.
#Implementar o método __main__ para incluir, alterar e excluir objetos destas contas, e
#ainda, chamada dos seus métodos específico.
#Utilizar o máximos dos conceitos vistos nas aulas anteriores.

#Caroline Caprini da Silveira - https://github.com/cprnn

def __main__():
    menu = 0
    opt= 0 
    aux = 0

    while menu != "0":
        print("Olá, bem vindo(a) ao banco! \n")
        print("1: Criar conta salário")
        print("2: Criar conta poupança")
        print("3: Criar conta especial")
        print("0: Sair")
        menu = input("Selecione:\n")

        if menu == "1":
            nome = input("Insira o nome:")
            conta = Salario(nome)

            while opt != "0":
                print("Selecione a operação:")
                print("1: Depósito")
                print("2: Saque") 
                print("3: Exibir saldo")
                print("0: Sair")
                aux = input("Selecione:\n")

                if aux == "1":
                    dep = int(input("Insira o valor a ser depositado:"))
                    response = conta.deposito(dep)
                    print(response)
                
                elif aux == "2":
                    saq = float(input("Insira o valor a ser sacado:"))
                    response = conta.saque(saq)
                    print(response)

                elif aux == "3":
                    print(conta.getSaldo())
                
                elif aux == "0":
                    print("Saindo.")
                    break

                else:
                    print("Não entendi. Insira novamente a opção:")
                    continue


        elif menu == "2":
            nome = input("Insira o nome:")
            conta = Poupanca(nome)

            while opt != "0":
                print("Selecione a operação:")
                print("1: Depósito")
                print("2: Saque") 
                print("3: Exibir saldo")
                print("4: Exibir rendimento")
                print("0: Sair")
                aux = input("Selecione:\n")

                if aux == "1":
                    dep = int(input("Insira o valor a ser depositado:"))
                    response = conta.deposito(dep)
                    print(response)

                elif aux == "2":
                    saq = float(input("Insira o valor a ser sacado:"))
                    response = conta.saque(saq)
                    print(response)

                elif aux == "3":
                    print(conta.getSaldo())

                elif aux == "3":
                    print(conta.getSaldo())
                
                elif aux == "0":
                    print("Saindo.")
                    break

                else:
                    print("Não entendi. Insira novamente a opção:")
                    continue
                    

        elif menu == "3":
            nome = input("Insira o nome:")
            conta = Especial(nome)

            while opt != "0":
                print("Selecione a operação:")
                print("1: Depósito")
                print("2: Saque") 
                print("3: Exibir saldo")
                print("0: Sair")
                aux = input("Selecione:\n")

                if aux == "1":
                    dep = float(input("Insira o valor a ser depositado:"))
                    response = conta.deposito(dep)
                    print(response)
                
                elif aux == "2":
                    saq = float(input("Insira o valor a ser sacado:"))
                    response = conta.saque(saq)
                    print(response)

                elif aux == "3":
                    print(conta.getSaldo())
                
                elif aux == "0":
                    print("Saindo.")
                    break

                else:
                    print("Não entendi. Insira novamente a opção:")
                    continue


        elif menu == "0":
            print("Obrigada por trabalhar conosco!")
            break
        else:
            print("Não entendi. Insira novamente a opção:")
            continue


#Classe main
class Conta: 

    def __init__(self, nome):
        self.nome = nome
        self.__saldo = 0.0
        print("Conta do cliente "+self.nome+" criada com sucesso!\n")

    def deposito(self,dep):
        if(dep>0):
            self.__saldo = self.__saldo + dep
            return "Depósito realizado com sucesso. Seu salto atual é de R$"+str(self.getSaldo())
        else:
            return "Não foi possível depositar este valor. Verifique se é maior que zero e repita a operação."

    def saque(self, valor):
        if(valor > 0):
            if((self.getSaldo() - valor)>=0):
                self.__saldo = self.__saldo - valor
                return "O valor "+str(valor)+" foi sacado de sua conta com sucesso! Seu saldo atual é de R$"+str(self.getSaldo())
            else:
                return "O valor solicitado não pode ser sacado, saldo insuficiente."
        else:
            return "Não é possível sacar um valor igual ou menor a zero."
    
    def getSaldo(self):
        return self.__saldo


#---------------------------------------------------------------------

class Salario(Conta):
    limite = 2000.00

    def __init__(self, nome):
        print("Atenção: O saque em caixa possui o limite de R$2000,00 por saque!")
        super().__init__(nome)
    

#---------------------------------------------------------------------

class Especial(Conta):
    limite = 500.0
    __cheque = 500.0

    def __init__(self, nome):
        super().__init__(nome)
        print("Atenção: Você pode sacar até R$500,00 acima de seu saldo atual, sendo descontado do cheque especial.")
        self.__debito = 0.0

    def saque(self, valor):
        saldo = self.getSaldo()

        if(valor <= saldo):
            return super().saque(valor)
        else:
            if((valor - saldo)<=self.__cheque):
                dif = (valor - saldo)
                self.__cheque = self.__cheque - dif
                self.__debito = dif
                
                print("O seu saque foi efetuado com sucesso. Seu débito atual é de R$ "+str(self.__cheque))
                return super().saque(valor - dif)
            else:
                return "A sua solicitação de saque não pode passar o seu limite de crédito. Seu limite no momento é R$"+str(self.limite)


#---------------------------------------------------------------------

class Poupanca(Conta):
    rende = 0,12

    def __init__(self, nome):
        print("Atenção: O saque possui o limite de R$2000,00!")
        super().__init__(nome)
    
    def rendimento(self, rende):
        self.__saldo = self.__saldo + (self.__saldo * rende)  #em implementação para a versão final

#---------------------------------------------------------------------

if __name__ == '__main__':
    __main__()