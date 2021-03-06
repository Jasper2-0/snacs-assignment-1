import cPickle as pickle

import numpy as np

import matplotlib
import matplotlib.pyplot as plt

MediumInFn = "pickles/Medium_In_Degree_Distribution.pickle"
MediumOutFn = 'pickles/Medium_Out_Degree_Distribution.pickle'

LargeInFn = 'pickles/Large_In_Degree_Distribution.pickle'
LargeOutFn = 'pickles/Large_Out_Degree_Distribution.pickle'

def main():
    
    
    MediumInDegreeDistribution = pickle.load(open(MediumInFn,'rb'))
    MediumOutDegreeDistribution = pickle.load(open(MediumOutFn,'rb'))
    
    LargeInDegreeDistribution = pickle.load(open(LargeInFn,'rb'))
    LargeOutDegreeDistribution = pickle.load(open(LargeOutFn,'rb'))
     
    xvalues = []
    
    for i in range(len(MediumInDegreeDistribution)):
        xvalues += [i]
    
    x = np.array(xvalues)
    y = np.array(MediumInDegreeDistribution)
    
    options = {}
    
    options["x"] = x;
    options["xlabel"] = 'In degrees'
    options["y"] = y;
    options["ylabel"] = 'frequency'
    options["title"] = 'In Degree Distribution Medium Network'
    options["filename"] = 'diagrams/Medium_In_Degree_Distribution.png'
    options['log'] = True
    
    graph(options);
    
    xvalues = []
    
    for i in range(len(MediumOutDegreeDistribution)):
        xvalues += [i]
    
    x = np.array(xvalues)
    y = np.array(MediumOutDegreeDistribution)
    
    options = {}
    
    options["x"] = x;
    options["xlabel"] = 'Out degrees'
    options["y"] = y;
    options["ylabel"] = 'frequency'
    options["title"] = 'Out Degree Distribution Medium Network'
    options["filename"] = 'diagrams/Medium_Out_Degree_Distribution.png'
    options['log'] = True
    
    graph(options);

    xvalues = []
    
    for i in range(len(LargeInDegreeDistribution)):
        xvalues += [i]
    
    x = np.array(xvalues)
    y = np.array(LargeInDegreeDistribution)
    
    options = {}
    
    options["x"] = x;
    options["xlabel"] = 'In degrees'
    options["y"] = y;
    options["ylabel"] = 'frequency'
    options["title"] = 'In Degree Distribution Large Network'
    options["filename"] = 'diagrams/Large_In_Degree_Distribution.png'
    options['log'] = True
    
    graph(options);

    xvalues = []
    
    for i in range(len(LargeOutDegreeDistribution)):
        xvalues += [i]
    
    x = np.array(xvalues)
    y = np.array(LargeOutDegreeDistribution)
    
    options = {}
    
    options["x"] = x;
    options["xlabel"] = 'Out degrees'
    options["y"] = y;
    options["ylabel"] = 'frequency'
    options["title"] = 'Out Degree Distribution Large Network'
    options["filename"] = 'diagrams/Large_Out_Degree_Distribution.png'
    options['log'] = True
    
    graph(options);


def graph(opts):
    fig = plt.figure()

    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

 
    axes.plot(opts['x'], opts['y'], 'r')

    axes.set_xlabel(opts['xlabel'])
    axes.set_ylabel(opts['ylabel'])
    if opts['log']: axes.set_yscale("log")
    axes.set_title(opts['title']);
    fig.savefig(opts['filename'])
    
main()