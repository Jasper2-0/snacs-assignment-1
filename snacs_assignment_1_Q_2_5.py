#!/usr/bin/env python
from graph_tool.all import *

import numpy as np
import cPickle as pickle


# /data is assumed to hold the provided graphs.

tinyFn = "data/tiny.in"
smallFn = "data/small.in"
mediumFn = "data/medium.in"
largeFn = "data/large.in"

def main():
    
    DGTiny = parseEdgeFileToDiGraph(tinyFn)

    l = graph_tool.topology.label_largest_component(DGTiny)
    u = graph_tool.topology.GraphView(DGTiny,vfilt=l)
    
    dist = graph_tool.stats.distance_histogram(u);
    
    dump(dist[0],'pickles/TinyDistance_Histogram.pickle');

    DGSmall = parseEdgeFileToDiGraph(smallFn)

    l = graph_tool.topology.label_largest_component(DGSmall)
    u = graph_tool.topology.GraphView(DGSmall,vfilt=l)
    
    print(u.num_vertices());
    
    dist = graph_tool.stats.distance_histogram(u);

    dump(dist[0],'pickles/Small_Distance_Histogram.pickle');
    
    DGMedium = parseEdgeFileToDiGraph(mediumFn)

    l = graph_tool.topology.label_largest_component(DGMedium)
    u = graph_tool.topology.GraphView(DGMedium,vfilt=l)
    
    print(u.num_vertices());
    
    dist = graph_tool.stats.distance_histogram(u);
    dump(dist[0],'pickles/Medium_Distance_Histogram.pickle');

    DGLarge = parseEdgeFileToDiGraph(largeFn)
    
    l = graph_tool.topology.label_largest_component(DGLarge)
    u = graph_tool.topology.GraphView(DGLarge,vfilt=l)
    
    print(u.num_vertices());
    
    dist = graph_tool.stats.distance_histogram(u);
    dump(dist[0],'pickles/Large_Distance_Histogram.pickle');

def parseEdgeFileToDiGraph( filename ):

    G = Graph()
    
    with open(filename,'r') as edgeFile:
        for line in edgeFile:
            line = line.rstrip('\n')
            v = line.split(" ")
            
            G.add_edge(v[0],v[1])

    return G

def dump(pickleVar, filename ):
    pickle.dump( pickleVar , open(filename,'wb'))

main()