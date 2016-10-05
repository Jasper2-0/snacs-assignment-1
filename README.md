    .------.            __         __    .-----.       __                        __    
    |   ___|-----.----.|__|.---.-.|  |   |   | |-----.|  |_.--.--.--.-----.----.|  |--.
    |___   |  _  |  __||  ||  _  ||  |   |     |  -__||   _|  |  |  |  _  |   _||    < 
    |______|_____|____||__||___._||__|   |_|___|_____||____|________|_____|__|  |__|__|
    .------.             __               __            ___              .-----.------.
    |  __  |-----.---.-.|  |.--.--.-----.|__|.-----.  .'  _|.-----.----. |   __|   ___|
    |      |     |  _  ||  ||  |  |__ --||  ||__ --|  |   _||  _  |   _| |  |__|___   |
    |__||__|__|__|___._||__||___  |_____||__||_____|  |__|  |_____|__|   |_____|______|
                            |_____|                                                    
    Leiden University 2016 - 2017 // Frank Takes // Govert Brinkmann
                           


# Assignment 1
This repository contains my work for the first assignment of the Social Network Analysis for Computer Scientists of Leiden University.



## Exercise 1: Neighborhoods (40p)

## Exercise 2: Mining an Online Social Network (60p)

### Q2.1 How many Directed links does this network have? | [snacs_assignment_1_Q_2_1.py](https://github.com/Jasper2-0/snacs-assignment-1/blob/master/snacs_assignment_1_Q_2_1.py)

- **Medium Network:** 12864
- **Large Network:** 1731653

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

### Q2.2 How many users does this network have?

- **Medium Network:** 2239
- **Large Network:** 279630


### Q2.3

### Q2.4 How many weakly conected components and how many strongly connected components does this network have? How many nodes and links are in the largest strongly connected component of this graph?

- **Number of weakly connected components Medium Network:** 9
- **Number of weakly connected components Large Network:** 6863

- **Number of strongly connected components Medium Network:** 9
- **Number of strongly connected components Large Network:** 240113


How many nodes are in the largest strongly connected component?

- **Medium Network:** 2217
- **Large Network:** 34826


How many links are in the largest strongly connected component?

- **Medium Network:** 12836
- **Large Network:** 799102

## Notes on elaborations

All  questions for exercise 2 were executed in Python. For each question an appropriate script was written. The script also takes care of reading in the edgelist, and producing the appropriate (directed) network.

    ~ local$: python snacs_assignment_1_Q_2_#.py

Where # is the question number. Each script produces markdown output, that was used to write the answers to the questions above.

I also added an extra network; 'Tiny' it's based on the 'Toy Network' that is used in lecture presentations. It allowed me to manually verify that my scripts were producing the intended output. 

For Questions 2.1 - 2.4 I used NetworkX to answer the questions. In the case of question 2.5, computing the distance distribution for the 'Large' network with NetworkX managed to turn my Macbook Pro into a functioning remote drone (read, fans were spinning so fast they managed to lift the laptop off my desk). Joking aside, Python / NetworkX quit after a total running time of an hour with an out of memory error. So, for answering question 2.5 I switched to using Graph-Tool. It produced the shortest distance distribution after 15 mins of computation on a single core. I wasn't able to install the OpenMP enabled version of graph-tool.


These can be found as q_2_3_[network]_in_degree.png and q_2_3_[network]_out_degree.png. 

Output reproduced below:
