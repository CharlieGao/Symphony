'''
Created on Mar 29, 2013

@author: Chutian
'''

import networkx as nw
import random
import math
import matplotlib.pyplot as plt


k=0 #N is the total number of nodes in the graph
k= int(input('Please input the number of k: '))
G=nw.Graph()


prefer=1# the chosen node
for nodes in range(0,k-1):
    x=random.randrange(0,nodes) #generate a random number x. x away from its own
    pn=1/((x/1000)*math.log1p(1000)) #probability distribution function
    #print(x)
'********************************************************'    
    divs=[]
    probs=[]
    for jndex in range (0,index-1):#computer prob
        probs.append((G.degree(jndex+1)/(2*(index+1))))
        if jndex !=0:
            divs.append(divs[jndex-1]+probs[jndex])            
        else:
            divs.append(probs[0])            
        if r<=divs[jndex]:
            prefer=jndex
            G.add_edge(jndex+1,prefer)
            break

    G.add_edge(index+1,prefer)
freq=nw.degree_histogram(G)
print("Edges are: ",G.edges())
'********************************************************'
def connectShort(nodeCurrent):
    """ this function is used for connecting short links with node 0 and last new node."""
    #break last new node with node 0
    G.remove_edge(nodeCurrent-1, 0)
    #link new node with last new node
    G.add_edge(nodeCurrent-1, nodeCurrent)
    #link new node with node 0
    G.add_edge(nodeCurrent, 0)
    G.node[nodeCurrent]['incoming'] = 1
    G.node[nodeCurrent]['outgoing'] = 1
'********************************************************'
'********************************************************'
def connectLong(nodeCurrent,nodeTarget):
    """ this function is used for connecting long links."""
    #link new node with nodeTarget
    G.add_edge(nodeCurrent, nodeTarget)
    G.node[nodeTarget]['incoming'] = G.node[nodeTarget]['incoming']+1
    G.node[nodeCurrent]['outgoing'] = G.node[nodeCurrent]['outgoing']+1
'********************************************************'
loogNk=[]
loogk=[]
loogNk_loogk=[]
k=freq.__len__()
for index in range(1,k):
    if freq[index]!=0:
        loogNk.append(math.log10(freq[index]))
        loogk.append(math.log10(index))
        

print("logNk= ",loogNk) 
print("logk= ",loogk)
plt.plot(loogk,loogNk,color='w',linestyle='-',marker='*')
plt.xlabel("Log k")
plt.ylabel("Log N(k)")
plt._show()

