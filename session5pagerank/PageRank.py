#!/usr/bin/python

from collections import namedtuple
import time
import sys

class Edge:
    def __init__ (self, origin=None):
        self.origin = origin 
        self.weight = 1 # write appropriate value

    def __repr__(self):
        return "edge: {0} {1}".format(self.origin, self.weight)
        
    ## write rest of code that you need for this class

class Airport:
    def __init__ (self, iden=None, name=None):
        self.code = iden    # codigo IATA
        self.name = name    
        self.routes = []        # routes: lista de edge; un edge es un aeropuerto con este como destimo: sristas de entrada
        self.routeHash = dict()     
        self.outweight = 0.0   # outdegree de este aeropuerto, inicialemnte a 0

    def __repr__(self):
        return f"{self.code}\t{self.pageIndex}\t{self.name}"

edgeList = [] # list of Edge
edgeHash = dict() # hash of edge to ease the match
airportList = [] # list of Airport
airportHash = dict() # hash key IATA code -> Airport

def readAirports(fd):
    print("Reading Airport file from {0}".format(fd))
    airportsTxt = open(fd, "r");
    cont = 0
    for line in airportsTxt.readlines():
        a = Airport()
        try:
            temp = line.split(',')
            if len(temp[4]) != 5 :
                raise Exception('not an IATA code')
            a.name=temp[1][1:-1] + ", " + temp[3][1:-1]
            a.code=temp[4][1:-1]
        except Exception as inst:
            pass
        else:
            cont += 1
            airportList.append(a)
            airportHash[a.code] = a
    airportsTxt.close()
    print(f"There were {cont} Airports with IATA code")

# escribe cada ruta a los aeropuertos
def readRoutes(fd):
    print("Reading Routes file from {0}".format(fd))
    routesTxt = open(fd, "r");
    cont = 0
    for line in routesTxt.readlines():
        try:
            temp = line.split(',')
            if len(temp[2]) != 3 or len(temp[4]) != 3:
                raise Exception('not an IATA code')
            originCode = temp[2]
            destCode = temp[4]
            if destCode in airportHash and originCode in airportHash:
                # for an edge (i.j), to compute pagerank we are only interested in which are the incoming edges for an airport
                destAirport = airportHash[destCode]
                destAirport.addIncomingEdge(originCode)
            else:
                raise Exception('inexistent Airports')

        except Exception as inst:
            pass
        else:
            cont += 1
    routesTxt.close()
    print("There were {0} Edges with both IATA code".format(cont))

            

def computePageRanks():
    # write your code

def outputPageRanks():
    # write your code

def main(argv=None):
    readAirports("airports.txt")
    readRoutes("routes.txt")
    time1 = time.time()
    iterations = computePageRanks()
    time2 = time.time()
    outputPageRanks()
    print("#Iterations:", iterations)
    print("Time of computePageRanks():", time2-time1)


if __name__ == "__main__":
    sys.exit(main())
