import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.flow import shortest_augmenting_path
import csv
# data plane A
GA = nx.Graph()

with open("sr-te-variables.csv") as csvFile:   #open the file
  CSVdata = csv.reader(csvFile, delimiter=',')  #read the data
  for row in CSVdata:   #loop through each row
    a = str(row[0])
    z = str(row[1])
    w = int(row[2])
    GA.add_edge(a, z, weight=w)

    print(a, z, w)  #print the data
csvFile.close()   #close the file



#
#GA.add_edge('ja', 'da', weight=10)
#GA.add_edge('ja', 'ta', weight=200)
#GA.add_edge('la', 'da', weight=10)
#GA.add_edge('la', 'ta', weight=10)
#GA.add_edge('la', 'ha', weight=10)
#GA.add_edge('ha', 'aa', weight=10)
#GA.add_edge('aa', 'ga', weight=200)
#GA.add_edge('aa', 'ta', weight=200)
#GA.add_edge('ta', 'da', weight=10)
#GA.add_edge('aa', 'ca', weight=10)
#GA.add_edge('da', 'ca', weight=10)
#GA.add_edge('ca', 'ga', weight=10)
#GA.add_edge('ga', 'ha', weight=10)
#GA.add_edge('ra', 'ca', weight=10)
#GA.add_edge('ra', 'ga', weight=200)

elarge = [(u, v) for (u, v, d) in GA.edges(data=True) if d['weight'] > 100]
esmall = [(u, v) for (u, v, d) in GA.edges(data=True) if d['weight'] <= 10]

posA={'ja':(0.4,0.8), 'da':(1,1), 'la':(0.4,-0.8), 'ta':(1,0), 'aa':(1,-0.7), 'ha':(1,-1.4), 'ga':(1.6,-0.5), 'ca':(1.4,0.5), 'ra':(2,0.5)}
# nodes
nx.draw_networkx_nodes(GA, posA, node_size=500, node_color='white',
        edgecolors='black')

# edges
#nx.draw_networkx_edges(GA, posA, width=2)
nx.draw_networkx_edges(GA, posA, edgelist=esmall, width=2, alpha=0.5,
        edge_color='blue', style='solid')
nx.draw_networkx_edges(GA, posA, edgelist=elarge, width=4, alpha=0.5,
        edge_color='blue', style='solid')

# labels
nx.draw_networkx_labels(GA, posA, font_size=9, font_family='sans-serif')

print('preplot')

plt.show()
