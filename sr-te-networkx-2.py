import matplotlib.pyplot as plt
import networkx as nx
import csv
import argparse

# add command line argument parsing
# --spf y = will show SPF for paths per path spreadsheet
parser = argparse.ArgumentParser()
parser.add_argument('-d', action='store_true', help='dijkstra spf')
# parser.add_argument('-f', action='store_true', help='load A to Z path from file')  <--remove file read for path
parser.add_argument('-p', help='src and dst nodes both planes - j d')
#parser.add_argument('-d', help='show dijkstra path = y')
args = parser.parse_args()
print(args.p)
# assign -p varibables to spf
if args.d == True:
    spfa1 = args.p[0]+"a"
    spfa2 = args.p[0]+"b"
    spfz1 = args.p[2]+"a"
    spfz2 = args.p[2]+"b"



# 2 data planes A (GA) and B (GB)
GA = nx.Graph()
GB = nx.Graph()

# read in edge data with with from csv file
with open("sr-te-variables.csv") as csvFile:    #open the file
  CSVdata = csv.reader(csvFile, delimiter=',')  #read the data
  for row in CSVdata:                           #loop through each row
    # A data plane
    a1 = str(row[0]) # source node - P router
    z1 = str(row[1]) # destination node - P router
    w1 = int(row[2]) # SR-TE metric
    # B data plane
    a2 = str(row[4]) # source node - P router
    z2 = str(row[5]) # destination node - P router
    w2 = int(row[6]) # SR-TE metric
    GA.add_edge(a1, z1, weight=w1)
    GB.add_edge(a2, z2, weight=w2)
csvFile.close()     #close the file

# read in A-Z Dijkstra path data from csv file
#if args.f == True:
#    with open("path-variables.csv") as csvFile:     #open the file
#      CSVdata = csv.reader(csvFile, delimiter=',')  #read the data
#      for row in CSVdata:                           #loop through each row
#        spfa1 = str(row[0])
#        spfz1 = str(row[1])
#        spfa2 = str(row[3])
#        spfz2 = str(row[4])
#    csvFile.close()     #close the file

# A data plane
# -----------------------------------------------------------------------------
# elarge to show exclude of path by using large SR-TE metric
# esmall for Dijkstra to destination prefix-SID
elarge = [(u, v) for (u, v, d) in GA.edges(data=True) if d['weight'] > 100]  # large edges
esmall = [(u, v) for (u, v, d) in GA.edges(data=True) if d['weight'] <= 10]  # small edges  

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
# edge lables
nx.draw_networkx_edge_labels(GA, posA, font_size=9, edge_labels={(a1, z1): w1})

# edge lables
#nx.draw_networkx_edge_labels(
#    GA, posA, font_size=9,
#    edge_labels={('ja', 'da'): weight})
#nx.draw_networkx_edge_labels(GA, posA, font_size=9, edge_labels={(a1, z1): w1})  # how to add label with weight

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


print('preplot')

# calculate and graph Dijkstra shortest path for GA
if args.d == True:
    print('spf if statment')
    pathsA = nx.dijkstra_path(GA, spfa1, spfz1, weight='weight')  # A Plane
    pathsA_edges = list(zip(pathsA,pathsA[1:]))
    nx.draw_networkx_edges(GA, posA, edgelist=pathsA_edges, width=3, alpha=0.5, edge_color='black', style='solid')
    pathsB = nx.shortest_path(GB, spfa2, spfz2, weight='weight')  # B Plane
    pathsB_edges = list(zip(pathsB,pathsB[1:]))
    nx.draw_networkx_edges(GB, posB, edgelist=pathsB_edges, width=3, alpha=0.5, edge_color='black', style='solid')


#print(nx.path_weight(GA, pathsA, 'weight'))
#draw_networkx_nodes
# total cost of path (edge+weight) for GA
#print(pathsA_edges) # print path pairs for SPF A plane
#print(pathsB_edges)




#for x in range(len(pathsA)):
#    print (pathsA[x])
#    print (len(pathsA[x]))

# edge lables
#nx.draw_networkx_edge_labels(
#    GA, posA, font_size=9,
#    edge_labels={('ja', 'da'): weight})

#for pathsA in nx.dijkstra_path(GA):
#    print(pathsA, len(pathsA))


#pathsA = nx.all_pairs_dijkstra(GA)
#print(pathsA)
#print(nx.path_weight(GA, pathsA, 'weight'))
#print(lengthsA)
#print('------------------')
#lengthsB = dict(nx.all_pairs_dijkstra(GB))
#print(lengthsB)


plt.show()
