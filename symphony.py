'''
Created on Mar 29, 2013

@author: Chutian
'''
'''
Created on Feb 11, 2013

@author: Chutian
'''
import networkx as nw
import random
import math
import matplotlib.pyplot as plt


N=0 #N is the total number of nodes in the graph
N= int(input('Please input the number of nodes that you want to generate: '))
G=nw.Graph()
#*******************************************************
"""
#The following code is for atoumaticly generate preferential attachment graph
G=nw.barabasi_albert_graph(N, 1)
print(G.edges())
freq=nw.degree_histogram(G)
print(freq)
"""
#*******************************************************

#index=0# node index
prefer=1# the chosen node
for index in range(1,N-1):
    r=random.randrange(100)/100
    #print(r)
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
#print(G.nodes()) 

#*****************************************************************#
#the following code is used to count the number of nodes with each degree (from 1 to N)
'''
number=[]
for j in range(0,N):    
    number.append(0)
#print(number)
for i in range(0,N):
    old=number[G.degree(i)-1]
    number.pop(G.degree(i)-1)
    number.insert(G.degree(i)-1,old+1)
print(number)
'''
#*****************************************************************#

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

