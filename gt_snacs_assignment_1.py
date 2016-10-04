#!/usr/bin/env python

import networkx as nx
import numpy as np

from graph_tool.all import *

import matplotlib.pyplot as plt

import cPickle as pickle

# /data is assumed to hold the provided graphs.

tinyFn = "data/tiny.in"
smallFn = "data/small.in"
mediumFn = "data/medium.in"
largeFn = "data/large.in"

large = True

global DGTiny
global DGSmall
global DGMedium
global DGLarge

global largestT
global largestS
global largestM
global largestL


def main():
    
    
    DGTiny = parseEdgeFileToDiGraph(tinyFn)
    DGMedium = parseEdgeFileToDiGraph(mediumFn)
    DGLarge = parseEdgeFileToDiGraph(largeFn)
    
    l = graph_tool.topology.label_largest_component(DGLarge)
    u = graph_tool.topology.GraphView(DGLarge,vfilt=l)
    
    print(u.num_vertices());
    
    dist = graph_tool.stats.distance_histogram(u);
    print dist


def parseEdgeFileToDiGraph( filename ):

    G = Graph()
    
    with open(filename,'r') as edgeFile:
        for line in edgeFile:
            line = line.rstrip('\n')
            v = line.split(" ")
            
            G.add_edge(v[0],v[1])

    return G

main()