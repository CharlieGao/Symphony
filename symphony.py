'''
Created on Mar 29, 2013

@author: Chutian
'''

import networkx as nw
import random
import math

k=0 #N is the total number of nodes in the graph
k=int(input('Please input the number of k: '))
G=nw.DiGraph()


def connectShort(pre,new):
    #link new node
    G.add_edge(new, pre)
    G.add_edge(pre, new)   
    return G
'********************************************************'
def connectLong(nodeCurrent,nodeTarget):
    """ this function is used for connecting long links."""
    #link new node with nodeTarget
    G.add_edge(nodeCurrent, nodeTarget)
    return G
'********************************************************'
def newNodeJoin(newNode):
    """new node joining to the circle"""      
    G.add_node(newNode)
    connectShort(newNode-1,newNode)#connect nodes
    return G 

def symphony(currentNode):           
    while G.out_degree(currentNode)<k+2:
        x=random.uniform(0, 1) #generate a random number x. x away from its own    
        ID=int(1000*math.exp(math.log(1000)*(x-1.0))) #implement PDF; pn=1/((x/1000)*math.log1p(1000)) probability distribution function
        
        if G.in_degree(ID)<2*k:
            if G.has_edge(currentNode, ID)|ID is currentNode:
                ID=ID #do nothing
            else:
                connectLong(currentNode,ID)  
                #print(ID)
    return G              

'********************************************************'
def printLinks(checkNode):
    sucs=G.successors(checkNode)
    #print(G.successors(checkNode))#all outgoing linked nodes
    print(sucs)
'********************************************************'
def computeRout(startNode,endNode):
    """compute rout Path starting from Start Node, using greedy method, unidirection"""      
    if endNode>startNode:
        #print(startNode)
        routList=[startNode]
        pred=startNode    
        while G.successors(pred).__contains__(endNode) is not True:
            sucs=G.successors(pred)
            #print(sucs)
            for i in range(0,k+2):
                if (sucs[i]>pred)&(sucs[i]<endNode):
                    pred=sucs[i]            
            #print(pred)
            routList.append(pred)
        #print(endNode)
        routList.append(endNode)
        print(routList)
    else:
        #print(startNode)
        routList=[startNode]
        pred=startNode    
        while G.successors(pred%999).__contains__(endNode) is not True:
            sucs=G.successors(pred%999)
            #print(sucs)
            for i in range(0,k+2):
                sucss=sucs[i]
                if (sucs[i]<endNode)&(sucs[i]>=0):
                    sucss=sucs[i]+999                    
                if (sucss>pred)&(sucss<endNode+999):
                    pred=sucss            
            #print(pred%999)
            routList.append(pred%999)
        #print(endNode)
        routList.append(endNode)
        print(routList)
'********************************************************'
G.add_node(0)
size=1
while size<1000:
    #newID=random.randrange(0,999) #generate a random number
    #if G.has_node(newID) is False:
    #newNodeJoin(size,size)
    newNodeJoin(size)
    size=size+1

G.add_edge(999,0)
G.add_edge(0,999)

for index in range(1000):   
    symphony(index)
'************************************************************************************'

printLinks(2)
printLinks(200)
printLinks(800)

print("*******************************************************************")
computeRout(2,700)
computeRout(800,10)
computeRout(500,100)
computeRout(90,891)
computeRout(200,600)

'********************************************************'

