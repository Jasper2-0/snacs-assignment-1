#!/usr/bin/env python
# 

mediumFn = "data/medium.in"

targetfile = "data/medium-gephiready.in"

def main():
    
    
    t = open(targetfile,'wb');
    
    t.write('Source\tTarget\tType')
    t.write('\n')
    
    with open(mediumFn,'r') as edgeFile:
        for line in edgeFile:
            line = line.rstrip('\n')
            v = line.split(" ")
            t.write(v[0]+"\t"+v[1]+"\t"+"Directed")
            t.write('\n')
    
    
    t.close()
    
    
    
main()