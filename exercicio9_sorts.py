#Exercício 9: Crie uma classe chamada de Ordenadora com os atributos básicos para uma tarefa de
#ordenamento. A seguir crie classes filhas que implementem os diversos métodos de
#ordenamento que estudamos na aula passada.

def menu():
    opt = 0

    while opt != "9":
        print("Inicie o algoritmo:")
        print("1: BubbleSort")
        print("2: SelectSort")
        print("3: QuickSort")
        print("9: Sair")
        opt = input("Selecione:\n")

        if opt == "1":
            toOrder = BubbleSort()
        elif opt == "2":
            toOrder = SelectSort()
        elif opt == "3":
            toOrder = QuickSort()
        elif opt == "9":
            break
        else:
            print("Insira novamente a opção:")
            continue

        print("Lista inicial:")
        print(list)
        print("Lista ordenada:")
        print(toOrder.sort())
        print("")

class Ordenadora:
    list= []

    def __init__(self):
        wdt = int(input('Digite a quantidade de elementos a serem ordenados:'))

        for i in range(wdt):
            print("Insira a lista de elementos a serem ordenados:")
            self.list.append(int(input("Valor("+str(i+1)+"):")))


#-------------------------------------------------------------------
#Bubble sort

class BubbleSort(Ordenadora):

    def __init__(self):
        super().__init__()

    def sort(self):
        ordered = self.list
        inOrder = False

        while not inOrder:
            inOrder = True
            for i in range(len(ordered)-1):
                if ordered[i]>ordered[i+1]:
                    ordered[i], ordered[i+1] = ordered[i+1], ordered[i]
                    inOrder = False
        return ordered


#-------------------------------------------------------------------
#Select sort

class SelectSort(Ordenadora):

    def __init__(self):
        super().__init__()

    def sort(self):
        ordered = self.list
        aux = len(ordered)

        for i in range(aux):
            low = aux-1
            for a in range(i, aux, 1):
                if ordered[a] < ordered[low]:
                    low = a
            ordered[i], ordered[low] = ordered[low], ordered[i]

        return ordered


#-------------------------------------------------------------------
#Quick sort

class QuickSort(Ordenadora):
    
    def __init__(self):
        super().__init__()

    def sort(self):
        inOrder = self.list
        return self.recFunction((inOrder))

    def recFunction(self, inOrder):
        if(len(inOrder) <= 1):
            return inOrder

        left, middle, right = [], [], []
        pivot = inOrder[0]

        for i in inOrder:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                middle.append(i)

        ordered = self.recFunction(left)
        ordered.extend(middle)
        ordered.extend(self.recFunction(right))
        return ordered

menu()