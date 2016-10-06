import cPickle as pickle

import numpy as np

import matplotlib
import matplotlib.pyplot as plt

MediumFn = "pickles/Medium_Distance_Histogram.pickle"
LargeFn = 'pickles/Large_Distance_Histogram.pickle'


def main():
    
    
    MediumHistogram= pickle.load(open(MediumFn,'rb'))
    LargeHistogram = pickle.load(open(LargeFn,'rb'))
    
    x = range(len(MediumHistogram))
    y = MediumHistogram

    fig = plt.figure()

    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)
    axes.bar(x,y,align='center',width=0.5)
    axes.set_xlabel('Distances')
    axes.set_ylabel('Count')
    axes.set_title('Distance Distribution Medium Network');
    fig.savefig("diagrams/Medium_Distance_Distribution.png")

    x = range(len(LargeHistogram))
    y = LargeHistogram

    fig = plt.figure()

    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)
    axes.bar(x,y,align='center',width=0.5)
    axes.set_xlabel('Distances')
    axes.set_ylabel('Count')
    axes.set_title('Distance Distribution Large Network');
    fig.savefig("diagrams/Large_Distance_Distribution.png")


main()