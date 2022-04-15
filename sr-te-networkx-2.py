import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.flow import shortest_augmenting_path
import csv

GA = nx.Graph()
GB = nx.Graph()

with open("sr-te-variables.csv") as csvFile:    #open the file
  CSVdata = csv.reader(csvFile, delimiter=',')  #read the data
  for row in CSVdata:                           #loop through each row
    a1 = str(row[0]) # source node - P router
    z1 = str(row[1]) # destination node - P router
    w1 = int(row[2]) # SR-TE metric
    a2 = str(row[4])
    z2 = str(row[5])
    w2 = int(row[6])
    GA.add_edge(a1, z1, weight=w1)
    GB.add_edge(a2, z2, weight=w2)
csvFile.close()     #close the file

with open("path-variables.csv") as csvFile:     #open the file
  CSVdata = csv.reader(csvFile, delimiter=',')  #read the data
  for row in CSVdata:                           #loop through each row
      spfa1 = str(row[0])
      spfz1 = str(row[1])
      spfa2 = str(row[3])
      spfz2 = str(row[4])
csvFile.close()     #close the file





# A data plane
# -----------------------------------------------------------------------------
# elarge to show exclude of path by using large SR-TE metric
# esmall for Dijkstra to destination prefix-SID
elarge = [(u, v) for (u, v, d) in GA.edges(data=True) if d['weight'] > 100]
esmall = [(u, v) for (u, v, d) in GA.edges(data=True) if d['weight'] <= 10]

# statically place nodes on graph
posA={'ja':(0.4,0.8), 'da':(1,1), 'la':(0.4,-0.8), 'ta':(1,0), 'aa':(1,-0.7), 'ha':(1,-1.4), 'ga':(1.6,-0.5), 'ca':(1.4,0.5), 'ra':(2,0.5)}

# configure nodes
nx.draw_networkx_nodes(GA, posA, node_size=500, node_color='white',
        edgecolors='black')
# label nodes
nx.draw_networkx_labels(GA, posA, font_size=9, font_family='sans-serif')

# draw edges between nodes with SR-TE metric weights
nx.draw_networkx_edges(GA, posA, edgelist=esmall, width=2, alpha=0.5,
        edge_color='blue', style='solid')
nx.draw_networkx_edges(GA, posA, edgelist=elarge, width=4, alpha=0.5,
        edge_color='blue', style='solid')



# B data plane
# -----------------------------------------------------------------------------
# elarge to show exclude of path by using large SR-TE metric
# esmall for Dijkstra to destination prefix-SID
elarge = [(u, v) for (u, v, d) in GB.edges(data=True) if d['weight'] > 100]
esmall = [(u, v) for (u, v, d) in GB.edges(data=True) if d['weight'] <= 10]

# statically place nodes on graph
posB={'jb':(2.4,0.8), 'db':(3,1), 'lb':(2.4,-0.8), 'tb':(3,0), 'ab':(3,-0.7), 'hb':(3,-1.4), 'gb':(3.6,-0.5), 'cb':(3.4,0.5), 'rb':(4,0.5)}

# configure nodes
nx.draw_networkx_nodes(GB, posB, node_size=500, node_color='white',
        edgecolors='black')
# label nodes
nx.draw_networkx_labels(GB, posB, font_size=9, font_family='sans-serif')

# draw edges between nodes with SR-TE metric weights
nx.draw_networkx_edges(GB, posB, edgelist=esmall, width=2, alpha=0.5,
        edge_color='red', style='solid')
nx.draw_networkx_edges(GB, posB, edgelist=elarge, width=4, alpha=0.5,
        edge_color='red', style='solid')

# Dijkstra shortest weighted path between two nodes
pathsA = nx.shortest_path(GA, spfa1, spfz1, weight='weight')  # A Plane
pathsA_edges = list(zip(pathsA,pathsA[1:]))
nx.draw_networkx_edges(GA, posA, edgelist=pathsA_edges, width=3, alpha=0.5, edge_color='black', style='solid')
pathsB = nx.shortest_path(GB, spfa2, spfz2, weight='weight')  # B Plane
pathsB_edges = list(zip(pathsB,pathsB[1:]))
nx.draw_networkx_edges(GB, posB, edgelist=pathsB_edges, width=3, alpha=0.5, edge_color='black', style='solid')


print('preplot')
plt.show()
