'''
Created on Mar 29, 2013

@author: Chutian
'''

import networkx as nw
import random
import math
import matplotlib.pyplot as plt

k=0 #N is the total number of nodes in the graph
k=int(input('Please input the number of k: '))
G=nw.DiGraph()


def connectShort(pre,new):
    ''''this function is used for connecting short links with node 0 and last new node.
    #break
    if G.has_edge(de, pre):
        G.remove_edge(de, pre)
        G.remove_edge(pre, de)
    #link new node 
    G.add_edge(new, de)
    G.add_edge(de, new)'''
    #link new node
    G.add_edge(new, pre)
    G.add_edge(pre, new)     
    #G.node[new]['outgoing'] = 2
    #G.node[precessor]['incoming'] = G.node[precessor]['incoming']+1
    #G.node[decessor]['incoming'] = G.node[decessor]['incoming']+1
    
    
    return G
'********************************************************'
def connectLong(nodeCurrent,nodeTarget):
    """ this function is used for connecting long links."""
    #link new node with nodeTarget
    G.add_edge(nodeCurrent, nodeTarget)
    #G.node[nodeTarget]['incoming'] = G.node[nodeTarget]['incoming']+1
    #G.node[nodeCurrent]['outgoing'] = G.node[nodeCurrent]['outgoing']+1
    return G
'********************************************************'
def newNodeJoin(newNode):
    """new node joining to the circle"""      
     
    #G.node[newNode]['outgoing'] = 0
    #G.node[newNode]['incoming'] = 0
                
    #precessor=G.node.__lt__(newNode)
    #decessor=G.node.__ge__(newNode)
    G.add_node(newNode)
    connectShort(newNode-1,newNode)#connect nodes
    return G 

def symphony(currentNode):           
    while G.out_degree(currentNode)<k+2:
        x=random.random() #generate a random number x. x away from its own    
        ID=int(1000*math.exp(math.log(1000)*(x-1.0))) #implement PDF; pn=1/((x/1000)*math.log1p(1000)) probability distribution function
        if G.in_degree(ID)<2*k:
            if G.has_edge(currentNode, ID):
                break
            else:
                connectLong(currentNode,ID)  
                #print(ID)
    return G  
            

'********************************************************'
def printLinks(checkNode):
    print(G.successors(checkNode))#all outgoing linked nodes
    
'********************************************************'
G.add_node(0)

size=1
while size<999:
    #newID=random.randrange(0,999) #generate a random number
    #if G.has_node(newID) is False:
    #newNodeJoin(size,size)
    newNodeJoin(size)
    size=size+1
G.add_node(999)
G.add_edge(999,0)
G.add_edge(0,999)

for index in range(1000):   
    symphony(index)
    
printLinks(0)

'''
nw.draw(G,pos=nw.random_layout(G))
plt.draw()
plt._show()
'''
'********************************************************'

