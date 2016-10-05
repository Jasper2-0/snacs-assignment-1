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

    # Q2.4 How many weakly conected components and how many strongly connected components
    # does this network have? How many nodes and links are in the largest strongly connected component of this graph?

    print "### Q2.4 How many weakly conected components and how many strongly connected components does this network have? How many nodes and links are in the largest strongly connected component of this graph?\n"
        
    print "Number of weakly connected components Tiny : " + str ( nx.number_weakly_connected_components(DGTiny) )
    print "Number of weakly connected components Small : " + str ( nx.number_weakly_connected_components(DGSmall) )
    print "Number of weakly connected components Medium : " + str ( nx.number_weakly_connected_components(DGMedium) )
    print "Number of weakly connected components Large : " + str ( nx.number_weakly_connected_components(DGLarge) )
    print "\n"
    
    print "Number of strongly connected components Tiny: " + str (nx.number_strongly_connected_components(DGTiny) )
    print "Number of strongly connected components Small: " + str (nx.number_strongly_connected_components(DGSmall) )
    print "Number of strongly connected components Medium: " + str (nx.number_strongly_connected_components(DGMedium) )
    print "Number of strongly connected components Large: " + str (nx.number_strongly_connected_components(DGLarge) )
    print "\n"
    
    largestT = max(nx.strongly_connected_component_subgraphs(DGTiny), key=len)
    largestS = max(nx.strongly_connected_component_subgraphs(DGSmall), key=len)
    largestM = max(nx.strongly_connected_component_subgraphs(DGMedium), key=len)
    largestL = max(nx.strongly_connected_component_subgraphs(DGLarge), key=len)
    
    print "How many nodes are in the largest strongly connected component?"
    print "Tiny Network: " + str ( nx.number_of_nodes(largestT) )
    print "Small Network: " + str ( nx.number_of_nodes(largestS) )
    print "Medium Network: " + str ( nx.number_of_nodes(largestM) )
    print "Large Network: " + str ( nx.number_of_nodes(largestL) )
    print "\n"
        
    print "How many links are in the largest strongly connected component?"
    print "Tiny Network: " + str ( nx.number_of_edges(largestT) )
    print "Small Network: " + str ( nx.number_of_edges(largestS) )
    print "Medium Network: " + str ( nx.number_of_edges(largestM) )
    print "Large Network: " + str ( nx.number_of_edges(largestL) )
    print "\n"
    
def parseEdgeFileToDiGraph( filename ):

    DG = nx.DiGraph()

    with open(filename,'r') as edgeFile:
        for line in edgeFile:
            line = line.rstrip('\n')
            v = line.split(" ")
            
            DG.add_edge(v[0],v[1])

    return DG

main()