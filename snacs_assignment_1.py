#!/usr/bin/env python

import networkx as nx
import numpy as np

import matplotlib.pyplot as plt

import cPickle as pickle

# /data is assumed to hold the provided graphs.

tinyFn = "data/tiny.in"
smallFn = "data/small.in"
mediumFn = "data/medium.in"
largeFn = "data/large.in"

large = True

global GTiny
global DGSmall
global DGMedium
global DGLarge

global largestT
global largestS
global largestM
global largestL


def main():

    global GTiny
    global DGSmall
    global DGMedium
    global DGLarge


    GTiny = parseEdgeFileToGraph(tinyFn)

    DGSmall = parseEdgeFileToDiGraph(smallFn)
    DGMedium = parseEdgeFileToDiGraph(mediumFn)
    if large: DGLarge = parseEdgeFileToDiGraph(largeFn)
    
    q21()
    q22()
 #   q23()
    q24()
    q25(largestM)
#    q25(largestL)
    
    
    
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

def InOutDegreeDistribution ( DiGraph ):
    inDegrees = DiGraph.in_degree().values()
    outDegrees = DiGraph.out_degree().values()
        
    InBinCount =  np.bincount(np.array(inDegrees))
    OutBinCount = np.bincount(np.array(outDegrees))
    
    plt.plot(InBinCount)
    plt.show()
    
    print "Count out degrees: "
    print "\n"


def q21():
    ## Q2.1 How many Directed links does this network have?
    
    print "### Q2.1 How many Directed links does this network have?"
    if not large: print "Small Network: " + str( nx.number_of_edges(DGSmall) )
    print "Medium Network: " + str( nx.number_of_edges(DGMedium) )
    if large: print "Large Network: " + str ( nx.number_of_edges(DGLarge) )
    print "\n"
    

def q22():
    ## Q2.2 How many users does this social network have?
    
    print "### Q2.2 How many users does this network have?"
    if not large: print "Small Network: " + str( nx.number_of_nodes(DGSmall) )
    print "Medium Network: " + str( nx.number_of_nodes(DGMedium) ) 
    if large: print "Large Network: " + str ( nx.number_of_nodes(DGLarge) )
    print "\n"
    
def q23():
    
    ## Q2.3 How many users does this social network have?
    
    print "### Q2.3 Give the indegree and outdegree distribution of this graph (so, for each degree value the number of times that it occurs)."
    InOutDegreeDistribution(DGMedium)
    if large: InOutDegreeDistribution(DGLarge)
    
    print "\n"    

def q24():
    # Q2.4 How many weakly conected components and how many strongly connected components
    # does this network have? How many nodes and links are in the largest strongly connected component of this graph?

    global largestT
    global largestS
    global largestM
    global largestL
    
    print "### Q2.4 How many weakly conected components and how many strongly connected components does this network have? How many nodes and links are in the largest strongly connected component of this graph?"
    print "\n"
        
    print "Number of weakly connected components Small : " + str ( nx.number_weakly_connected_components(DGSmall) )
    print "Number of weakly connected components Medium : " + str ( nx.number_weakly_connected_components(DGMedium) )
    if large: print "Number of weakly connected components Large : " + str ( nx.number_weakly_connected_components(DGLarge) )
    print "\n"
    
    print "Number of strongly connected components Small: " + str (nx.number_strongly_connected_components(DGSmall) )
    print "Number of strongly connected components Medium: " + str (nx.number_strongly_connected_components(DGMedium) )
    if large: print "Number of strongly connected components Large: " + str (nx.number_strongly_connected_components(DGLarge) )
    print "\n"
    
    largestS = max(nx.strongly_connected_component_subgraphs(DGSmall), key=len)
    largestM = max(nx.strongly_connected_component_subgraphs(DGMedium), key=len)
    if large: largestL = max(nx.strongly_connected_component_subgraphs(DGLarge), key=len)
    
    print "How many nodes are in the largest strongly connected component?"
    print "Small Network: " + str ( nx.number_of_nodes(largestS) )
    print "Medium Network: " + str ( nx.number_of_nodes(largestM) )
    if large: print "Large Network: " + str ( nx.number_of_nodes(largestL) )
    print "\n"    
    
    
    print "How many links are in the largest strongly connected component?"
    if not large: print "Small Network: " + str ( nx.number_of_edges(largestS) )
    print "Medium Network: " + str ( nx.number_of_edges(largestM) )
    if large: print "Large Network: " + str ( nx.number_of_edges(largestL) )
    print "\n"

def q25(graph):
    shortest_paths = nx.all_pairs_shortest_path(graph)

    print "done sp"
    
    flatCount = []
    
    for key in shortest_paths['10']:
        for path in shortest_paths[key]:
            flatCount += [len(shortest_paths[key][path])]
    
    counts = np.array(flatCount)
    print np.bincount(counts)
    print np.sum(counts)
    
    
    
    


def dump(pickleVar, filename ):
    pickle.dump( pickleVar , open(filename,'wb'))
    

main()