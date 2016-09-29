#!/usr/bin/env python
# /data is assumed to hold the provided graphs.

import networkx as nx

smallFn = "data/small.in"
mediumFn = "data/medium.in"
largeFn = "data/large.in"

large = False

def main():

    selectedFile = largeFn;
    
    DGSmall = parseEdgeFileToDiGraph(smallFn)
    DGMedium = parseEdgeFileToDiGraph(mediumFn)
    if (large): DGLarge = parseEdgeFileToDiGraph(largeFn)

    
    
    
    


    # Q2.1 How many Directed links does this network have?
    
    print "### Q2.1 How many Directed links does this network have?"
    print "Small Network: " + str( nx.number_of_edges(DGSmall) )
    print "Medium Network: " + str( nx.number_of_edges(DGMedium) )
    if (large): print "Large Network: " + str ( nx.number_of_edges(DGLarge) )
    print "\n"
    
    # Q2.2 How many users does this social network have?
    
    print "### Q2.2 How many users does this network have?"
    print "Small Network: " + str( nx.number_of_nodes(DGSmall) )
    print "Medium Network: " + str( nx.number_of_nodes(DGMedium) ) 
    if (large): print "Large Network: " + str ( nx.number_of_nodes(DGLarge) )
    print "\n"
    
    # Q2.4 How many weakly conected components and how many strongly connected components
    # does this network have? How many nodes and links are in the largest strongly connected component of this graph?

    print "### Q2.4 How many weakly conected components and how many strongly connected components does this network have? How many nodes and links are in the largest strongly connected component of this graph?"
    print "\n"

    print "Number of weakly connected components: "
    print "Small Network: " + str ( nx.number_weakly_connected_components(DGSmall) )
    print "Medium Network: " + str (nx.number_weakly_connected_components(DGMedium) )
    if (large): print "Large Network: " + str (nx.number_weakly_connected_components(DGLarge) )
    print "\n"

    print "Number of strongly connected components: "
    print "Small Network: " + str (nx.number_strongly_connected_components(DGSmall) )
    print "Medium Network: " + str (nx.number_strongly_connected_components(DGMedium) )
    if (large): print "Large Network: " + str (nx.number_strongly_connected_components(DGLarge) ) 
    print "\n"
    
    largestS = max(nx.strongly_connected_components(DGSmall), key=len)
    largestM = max(nx.strongly_connected_components(DGMedium), key=len)
    if (large): largestL = max(nx.strongly_connected_components(DGLarge), key=len)


    
    gCS = nx.DiGraph()
    gCM = nx.DiGraph()
    if (large): gCL = nx.DiGraph()
    
    gCS.add_nodes_from(largestS)
    gCM.add_nodes_from(largestM)
    if (large): gCL.add_nodes_from(largestL)
    
    
    print "How many nodes are in the largest strongly connected component?"
    print "Small Network: " + str ( nx.number_of_nodes(gCS) )
    print "Medium Network: " + str ( nx.number_of_nodes(gCM) )
    if (large): print "Large Network: " + str ( nx.number_of_nodes(gCL) )
    print "\n"    
#
#
#   print "How many links are in the largest strongly connected component?"
#   print "Small Network: " + str ( nx.number_of_edges(gCS) )
#   print "Medium Network: " + str ( nx.number_of_edges(gCM) )
#   if (large): print "Large Network: " + str ( nx.number_of_edges(gCL) )
#   print "\n"    

    
def parseEdgeFileToGraph ( filename ):

    # create empty graph
    G = nx.Graph();
    
    with open(filename,'r') as edgeFile:
        
        for line in edgeFile:
            line = line.rstrip('\n') 
            v = line.split(" ");
            
            G.add_edge(v[0],v[1])
            
    return G


def parseEdgeFileToDiGraph( filename ):

    DG = nx.DiGraph()
    
    with open(filename,'r') as edgeFile:
        for line in edgeFile:
            line = line.rstrip('\n')
            v = line.split(" ")
            
            DG.add_edge(v[0],v[1])

    return DG

main()