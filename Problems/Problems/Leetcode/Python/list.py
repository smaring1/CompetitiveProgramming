class Node:
    def __init__(self, data):
        _next = None
        _data = data

class ListaSimon:
    def __init__(self):
        self.first = None
        self.size = 0

    def getNodo(self, index):
        temp = self.first
        for i in range(index):
            temp = temp.next
        return temp


    def get(self, index):
        temp = self.first
        for i in range(index):
            temp = temp.next
        return temp.data
    
    def addFirst(self,e):

        #pasos para agregar al inicio
        #crear un nodo con el elemento adentro
        nodoNuevo = Node(e) 
        #El siguiente del nodo es el primero que teniamos
        nodoNuevo.next = self.first 
        #el nuevo nodo va a ser el primero
        self.first = nodoNuevo
        
    def add(self, e, i):
        if i == 0:
            addFirst(e)
        else:
            nodoIMenosUno = self.getNodo(i-1)
            nodoNuevo = Node(e) 
            temp = nodoIMenosUno.next
            nodoIMenosUno.next = nodoNuevo
            nodoNuevo.next = temp

    def contains(self,e): #Simon dice que se dana la lista
        temp = self.first
        while (temp == None):
            if (temp.data == e):
                return True
            temp = temp.next
        return False