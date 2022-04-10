import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.flow import shortest_augmenting_path

# data plane A
GA = nx.Graph()

GA.add_edge('ja', 'da', weight=10)
GA.add_edge('ja', 'ta', weight=10)
GA.add_edge('la', 'da', weight=10)
GA.add_edge('la', 'ta', weight=10)
GA.add_edge('la', 'ha', weight=10)
GA.add_edge('ha', 'aa', weight=10)
GA.add_edge('aa', 'ga', weight=10)
GA.add_edge('aa', 'ta', weight=10)
GA.add_edge('ta', 'da', weight=10)
GA.add_edge('aa', 'ca', weight=10)
GA.add_edge('da', 'ca', weight=10)
GA.add_edge('ca', 'ga', weight=10)
GA.add_edge('ga', 'ha', weight=10)
GA.add_edge('ra', 'ca', weight=10)
GA.add_edge('ra', 'ga', weight=10)

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

# dijkstra shortest weighted path between two nodes
pathsA = nx.shortest_path(GA, 'ja', 'ra', weight='weight')
pathsA_edges = list(zip(pathsA,pathsA[1:]))
nx.draw_networkx_edges(GA, posA, edgelist=pathsA_edges, width=2, alpha=0.5, edge_color='black',
        style='solid')
#flow = shortest_augmenting_path(G, 'j', 'r', capacity = 5)
print("A_plane_SPF: ", pathsA)
#print(flow)
plt.axis('off')
#plt.show()

#=================================================

# data plane B

GB = nx.Graph()

GB.add_edge('jb', 'db', weight=200)
GB.add_edge('jb', 'tb', weight=10)
GB.add_edge('lb', 'db', weight=10)
GB.add_edge('lb', 'tb', weight=10)
GB.add_edge('lb', 'hb', weight=10)
GB.add_edge('hb', 'ab', weight=10)
GB.add_edge('ab', 'gb', weight=10)
GB.add_edge('ab', 'tb', weight=10)
GB.add_edge('tb', 'db', weight=10)
GB.add_edge('ab', 'cb', weight=10)
GB.add_edge('db', 'cb', weight=200)
GB.add_edge('cb', 'gb', weight=10)
GB.add_edge('gb', 'hb', weight=10)
GB.add_edge('rb', 'cb', weight=200)
GB.add_edge('rb', 'gb', weight=10)

elarge = [(u, v) for (u, v, d) in GB.edges(data=True) if d['weight'] > 100]
esmall = [(u, v) for (u, v, d) in GB.edges(data=True) if d['weight'] <= 10]

posB={'jb':(2.4,0.8), 'db':(3,1), 'lb':(2.4,-0.8), 'tb':(3,0), 'ab':(3,-0.7), 'hb':(3,-1.4), 'gb':(3.6,-0.5), 'cb':(3.4,0.5), 'rb':(4,0.5)}
# nodes
nx.draw_networkx_nodes(GB, posB, node_size=500, node_color='white',
        edgecolors='black')  

# edges
#nx.draw_networkx_edges(GB, posB, width=2)
nx.draw_networkx_edges(GB, posB, edgelist=esmall, width=2, alpha=0.5,
        edge_color='red', style='solid')
nx.draw_networkx_edges(GB, posB, edgelist=elarge, width=4, alpha=0.5,
        edge_color='red', style='solid')

# labels
nx.draw_networkx_labels(GB, posB, font_size=9, font_family='sans-serif')

# dijkstra shortest weighted path between two nodes
pathsB = list(nx.dijkstra_path(GB, 'jb', 'rb', weight='weight'))

#flow = shortest_augmenting_path(G, 'j', 'r', capacity = 5)
print("B_plane_SPF: ", pathsB)
#print(flow)
plt.axis('off')
plt.show()
