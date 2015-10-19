'''
Created on Oct 12, 2015

@author: pta
'''

import csv

def read_data(file_path):
    
    lines = open(file_path, 'r').readlines()
    data=[]

    keys= lines[0].strip().split(',')
    
#     print keys
    for line in lines[1:]:
        vs = line.strip().split(',')
        sample={}
        for k,v in zip(keys, vs):
            sample[k]=v
        data.append(sample)
            
    return data
    
if __name__ == '__main__':
    data = read_data('alarm.csv')
    
    from libpgm.nodedata import NodeData
    from libpgm.graphskeleton import GraphSkeleton
    from libpgm.discretebayesiannetwork import DiscreteBayesianNetwork
    from libpgm.pgmlearner import PGMLearner
    from libpgm import dyndiscbayesiannetwork
    from libpgm import hybayesiannetwork
    from libpgm import lgbayesiannetwork
    
    learner = PGMLearner()
    
    result = learner.discrete_constraint_estimatestruct(data)
    
    print result.E 
#     print data
    
    