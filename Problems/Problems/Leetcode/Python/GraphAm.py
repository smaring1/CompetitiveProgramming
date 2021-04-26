class GraphAm:
    def __init__(self, size):
        self.graph = [[]]


    def getWeight(self, source, destination):
        return self.graph[source][destination]

    def addArc(self, source, destination, weight):
        self.graph[source][destination] = weight

    def getSuccessors(self, vertex):
        sucessors = []
        for i in range(0, self.graph[vertex]):
            if self.graph[vertex][i] > 0:
                sucessors.append(i)
        return sucessors

#    def __str__(self):
