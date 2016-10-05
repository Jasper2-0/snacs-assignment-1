#!/usr/bin/env python

import networkx as nx
import numpy as np

# /data is assumed to hold the provided graphs.

tinyFn = "data/tiny.in" # tiny network, for learning / debugging purposes
smallFn = "data/small.in"
mediumFn = "data/medium.in"
largeFn = "data/large.in"

def main():

    DGTiny = parseEdgeFileToDiGraph(tinyFn)
    DGSmall = parseEdgeFileToDiGraph(smallFn)
    DGMedium = parseEdgeFileToDiGraph(mediumFn)
    DGLarge = parseEdgeFileToDiGraph(largeFn)

    ## Q2.1 How many Directed links does this network have?
    
    print "### Q2.1 How many Directed links does this network have?"
    print "Tiny Network: " + str( nx.number_of_edges(DGTiny) )
    print "Small Network: " + str( nx.number_of_edges(DGSmall) )
    print "Medium Network: " + str( nx.number_of_edges(DGMedium) )
    print "Large Network: " + str ( nx.number_of_edges(DGLarge) )
    
def parseEdgeFileToDiGraph( filename ):

    DG = nx.DiGraph()

    with open(filename,'r') as edgeFile:
        for line in edgeFile:
            line = line.rstrip('\n')
            v = line.split(" ")
            
            DG.add_edge(v[0],v[1])

    return DG

main()