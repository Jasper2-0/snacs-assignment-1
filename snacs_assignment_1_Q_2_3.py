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

    ## "### Q2.3 Give the indegree and outdegree distribution of this graph (so, for each degree value the number of times that it occurs)."
    
    print "### Q2.3 Give the indegree and outdegree distribution of this graph (so, for each degree value the number of times that it occurs).\n"
    print "In Degree Distribution Tiny Network: "+ str(InDegreeDistribution(DGTiny))
    print "Out Degree Distribution Tiny Network: "+ str(OutDegreeDistribution(DGTiny))
    print ""
    print "In Degree Distribution Small Network: "+ str(InDegreeDistribution(DGSmall))
    print "Out Degree Distribution Small Network: "+ str(OutDegreeDistribution(DGSmall))
    print ""
    print "In Degree Distribution Medium Network: "+ str(InDegreeDistribution(DGMedium))
    print "Out Degree Distribution Medium Network: "+ str(OutDegreeDistribution(DGMedium))
    print ""
    print "In Degree Distribution Large Network: "+ str(InDegreeDistribution(DGLarge))
    print "Out Degree Distribution Large Network: "+ str(OutDegreeDistribution(DGLarge))


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

main()