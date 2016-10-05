#!/usr/bin/env python

import networkx as nx
import numpy as np

import cPickle as pickle

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

    ## "### Q2.3 Give the indegree and outdegree distribution of this graph (so, for each degree value the number of times that it occurs)."
    
    print "### Q2.3 Give the indegree and outdegree distribution of this graph (so, for each degree value the number of times that it occurs).\n"

    tinyInDistribution = InDegreeDistribution (DGTiny)
    dump (tinyInDistribution,'pickles/Tiny_In_Degree_Distribution.pickle');
    
    tinyOutDistribution = OutDegreeDistribution (DGTiny)
    dump (tinyOutDistribution,'pickles/Tiny_Out_Degree_Distribution.pickle');

    SmallInDistribution = InDegreeDistribution (DGSmall)
    dump (SmallInDistribution,'pickles/Small_In_Degree_Distribution.pickle');
    
    SmallOutDistribution = OutDegreeDistribution (DGSmall)
    dump (SmallOutDistribution,'pickles/Small_Out_Degree_Distribution.pickle');

    MediumInDistribution = InDegreeDistribution (DGMedium)
    dump (MediumInDistribution,'pickles/Medium_In_Degree_Distribution.pickle');
    
    MediumOutDistribution = OutDegreeDistribution (DGMedium)
    dump (MediumOutDistribution,'pickles/Medium_Out_Degree_Distribution.pickle');

    LargeInDistribution = InDegreeDistribution (DGLarge)
    dump (LargeInDistribution,'pickles/Large_In_Degree_Distribution.pickle');
    
    LargeOutDistribution = OutDegreeDistribution (DGLarge)
    dump (LargeOutDistribution,'pickles/Large_Out_Degree_Distribution.pickle');


def InDegreeDistribution ( DiGraph ):
    inDegrees = DiGraph.in_degree().values()
        
    InBinCount =  np.bincount(np.array(inDegrees))
    
    return InBinCount

def OutDegreeDistribution ( DiGraph ):
    outDegrees = DiGraph.out_degree().values()
    OutBinCount = np.bincount(np.array(outDegrees))
    
    return OutBinCount

def parseEdgeFileToDiGraph( filename ):

    DG = nx.DiGraph()

    with open(filename,'r') as edgeFile:
        for line in edgeFile:
            line = line.rstrip('\n')
            v = line.split(" ")
            
            DG.add_edge(v[0],v[1])

    return DG

def dump(pickleVar, filename ):
    pickle.dump( pickleVar , open(filename,'wb'))

main()