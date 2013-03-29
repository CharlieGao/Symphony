'''
Created on Mar 29, 2013

@author: Chutian
'''
'''
Created on Feb 12, 2013

@author: Chutian
'''
import networkx as nw
import matplotlib.pyplot as plt


G=nw.karate_club_graph()

nw.draw(G,pos=nw.spring_layout(G))
plt.draw()

def on_button_press(event):
    
      
    bb=nw.edge_betweenness_centrality(G)    
    big=max(bb, key=bb.get)    
    G.remove_edge(big[0],big[1])
    print(big)
    plt.clf()
    
    nw.draw(G,pos=nw.spring_layout(G))    
    plt.draw()
    
plt.gcf().canvas.mpl_connect("button_press_event", on_button_press)
plt._show()

"""
'''*******************************************************************************'''
big=0
ipt= input('Type Y to delete the highest betweenness edge; N do Nothing : ')
if ipt=='Y' or ipt=='y':
    bb=nw.edge_betweenness_centrality(G)
    
    big=max(bb, key=bb.get)    
    G.remove_edge(big[0],big[1]) 
    #nw.draw(G)
    plt.show()
else:
    print(big)
    #nw.draw(G)
    #plt.show()
"""