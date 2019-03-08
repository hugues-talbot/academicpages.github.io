from copy import deepcopy

## a graph class
## Hugues Talbot
## 2017-10-11

import matplotlib.pylab as plt
import numpy as np
import csv
from copy import deepcopy

## a graph class
class Graph(object):
    """A simple graph structure"""    
    def __init__(self,edges,nodes,W,H):
        self.edges = deepcopy(edges)
        self.nodes = deepcopy(nodes)
        self.W = W
        self.H = H
        self.Size = 1/max(W,H) ## size of a square pixel
        self.Epsilon = 0.05*self.Size
        self.Delta = 0.5*self.Size ## to center circles
        pass

    # return only a shallow copy (pointer) to the edges
    def get_edges(self):
        return(self.edges)

    # shallow copy to the nodes
    def get_nodes(self):
        return(self.nodes)

    def get_W(self):
        return(self.W)
    
    def get_H(self):
        return(self.H)
    
    def get_dims(self):
        return(self.W,self.H)
    
    def xyToIndex(self,x,y):
        return(y*self.W+x)
    
    def pdot(self,x,y,col,full=False):
        if full:
            plt.gcf().gca().add_artist(plt.Circle((x,y),0.5*self.Delta,ec=col,color=col))
        else:
            plt.gcf().gca().add_artist(plt.Circle((x,y),0.5*self.Delta,ec=col,color='white'))
    
    def psquare(self,x,y,col,full=False):
        if full:
            plt.gcf().gca().add_artist(plt.Rectangle((x,y),self.Size,self.Size,ec=col,color=col))
        else:
            plt.gcf().gca().add_artist(plt.Rectangle((x,y),self.Size,self.Size,ec=col,color='white'))
    
    def plotNodes(self):
        for n in self.nodes:
            x = n[0] ; y = n[1]
            ## le +0.5*self.Size) est purement cosmetique
            self.pdot(x+self.Delta,y+self.Delta,col='green',full=n[2])
            
    def plotSquares(self,neg=False,bin=False):
        if (bin):
            for n in self.nodes:
                if (neg):
                    if (n[2]>0):
                        x = n[0] ; y = n[1]+self.Epsilon
                        self.psquare(x,y,col='black',full=True)
                else:
                    if (n[2]==0):
                        x = n[0] ; y = n[1]+self.Epsilon
                        self.psquare(x,y,col='black',full=True)
        else:
            for n in self.nodes:
                x = n[0] ; y = n[1]+self.Epsilon
                self.psquare(x,y,col='green',full=n[2])
             
    def plotEdges(self):
        for e in self.edges:
            n1 = self.nodes[e[0]]
            n2 = self.nodes[e[1]]
            x1 = n1[0]+self.Delta ; x2 = n2[0]+self.Delta
            y1 = n1[1]+self.Delta ; y2 = n2[1]+self.Delta
            plt.arrow(x1,y1,(x2-x1),(y2-y1),fc='k',ec='k')
    
    # display with edges
    def display(self):
        plt.figure(figsize=(8,8))
        ax=plt.subplot(aspect='equal')
        plt.gcf().gca().invert_yaxis() ## to plot in the usual way for images
        plt.axis('off')
        self.plotEdges()
        self.plotNodes()
        plt.show()
        
    # display as pixels
    def pixels(self):
        plt.figure(figsize=(8,8))
        ax=plt.subplot(aspect='equal')
        plt.axis('off')
        plt.gcf().gca().invert_yaxis() ## to plot in the usual way for images
        self.plotSquares()
        plt.show()    
        
    ## exporte un buffer numpy
    def image(self, dtype=np.uint8):
        a = np.zeros(self.W*self.H,dtype=dtype)
        i=0
        for n in self.nodes:
            a[i] = n[2]
            i+=1
        return(a.reshape(self.H,self.W))
    
    ## plot avec numpy
    def show(self,inv=False):
        plt.figure(figsize=(8,8))
        ax=plt.subplot(aspect='equal')
        plt.axis('off')
        if (inv):
            plt.imshow(self.image(),cmap="gray_r")
        else:
            plt.imshow(self.image(),cmap="gray")
        plt.show()
        
        
def appyDualNodeOperator(g1,g2, dual_op_, verify=True):
    """
    applies a generic scalar Dual operator on the nodes of G1 and G2 and returns a new graph
    
    applique un operateur sur les sommets de deux graphes G1 et G2 et produit un nouveau graphe
    
    """
    mynodes_out = deepcopy(g1.get_nodes())
    mynodes_in = g2.get_nodes() # read only, no need to copy
    W = g1.get_W()
    H = g1.get_H()
    if (not verify):
        for i in range(0,W*H):
            mynodes_out[i][2] = dual_op_(my_nodes_out[i][2],my_nodes_in[i][2])
    else:
        for i in range(0,g1.get_H()*g1.get_W()):
            if ((mynodes_out[i][0] == mynodes_in[i][0]) and (mynodes_out[i][1] == mynodes_in[i][1])): 
                mynodes_out[i][2] = dual_op_(mynodes_out[i][2],mynodes_in[i][2])
    return(Graph(g1.get_edges(), mynodes_out, W,H))   


                                   
        
def createEmptyGraph(W,H):
    '''
    Creation d'un graphe rectangulaire vide
    '''
    ## pour que le graphe entier puisse tenir sur la figure
    wh = max(W,H)+1 # the +1 is so the entire figure is visible up to the edges

    nodes=[] ## structure de sommets: une liste

    ## les sommets du graphe (nodes en anglais)
    ## on va faire apparaître les pixel avec des carrés, donc
    ## inutile de rajouter le facteur 1/(2wh) à chaque coordonnée.
    for y in range(0,H):
        for x in range(0,W):
            ## un sommet = 2 coordonnées + une valeur 
            nodes.append([float(x)/(wh),
                        float(y)/(wh),0]) 
            
    edges = [] ## structure d'arêtes

    for y in range(0,H-1):
        for x in range(0,W-1):
            i = y * W + x
            edges.append([i,i+1,0]) # toutes les arêtes sont valuées à zéro 
            edges.append([i,i+W,0]) # pour le moment

    # arêtes de la fin
    for x in range(0,W-1):
        i = (H-1)*W + x
        edges.append([i,i+1,0])
    for y in range(0,H-1):
        i = y * W + (W-1)
        edges.append([i,i+W,0])
    
    return(edges,nodes)

def read_graph(file,verbose=False):
    '''
    Read a graph from a file
    '''
    f = open(file)
    result = csv.reader(f,delimiter=' ')
    i = 0
    k = 0
    try:
        for row in result:
            if (verbose):
                print(row)
            if (i==0): ## first row
                dimX=int(row[0])
                dimY=int(row[1])
                print("Graphe de dimension (%d x %d)" % (dimX,dimY))
                edges,nodes=createEmptyGraph(dimX,dimY)
                i = 1
            else:
                for element in row:
                    nodes[k][2] = int(element)
                    k = k+1
    except:
        print("*** Exception: k=%d" % k)
    return(Graph(edges,nodes,dimX,dimY))


## Dilation by considering the adjacency graph
## Dilation by considering the adjacency graph
def dilate(g1):
    ## input edges (deep copied)
    myedges = g1.get_edges()
    mynodes_in = g1.get_nodes()
    ## output edges
    mynodes_out = deepcopy(mynodes_in)
    ## not elegant
    for n in myedges:
        v1 = mynodes_in[n[0]][2] # value
        v2 = mynodes_in[n[1]][2]
        maxv = max(v1,v2)
        ## change la valeur de la sortie si elle est plus grande
        mynodes_out[n[0]][2] = max(maxv, mynodes_out[n[0]][2])
        mynodes_out[n[1]][2] = max(maxv, mynodes_out[n[1]][2])
    ## 
    return(Graph(myedges,mynodes_out,g1.get_W(),g1.get_H()))

## Erosion by considering the adjacency graph
def erode(g1):
    ## input edges (deep copied)
    myedges = g1.get_edges()
    mynodes_in = g1.get_nodes()
    ## output edges
    mynodes_out = deepcopy(mynodes_in)
    ## not elegant
    for n in myedges:
        v1 = mynodes_in[n[0]][2] # value
        v2 = mynodes_in[n[1]][2]
        minv = min(v1,v2)
        mynodes_out[n[0]][2] = min(minv,mynodes_out[n[0]][2])
        mynodes_out[n[1]][2] = min(minv,mynodes_out[n[1]][2])
    ## 
    return(Graph(myedges,mynodes_out, g1.get_W(), g1.get_H()))

def ouverture(g1):
    return(dilate(erode(g1)))
          
def fermeture(g1):
    return(erode(dilate(g1)))
    
def changeAdjacency(graph,type='4'):
    '''
    Change l'adjacence d'un graphe:
    type = '4' -> 4-connexe
    type = '8' -> 8-connexe
    type = 'H' -> horizontal
    type = 'V' -> vertical
    type = 'D1' -> diagonal nw-se
    type = 'D2' -> diagonal ne-sw
    '''
    nodes=graph.get_nodes() ## récupère les sommets
    W = graph.get_W()
    H = graph.get_H()
            
    edges = [] ## structure d'arêtes
    
    ## "4-connectivité"
    if (type == '4'):
        for y in range(0,H-1):
            for x in range(0,W-1):
                i = y * W + x
                edges.append([i,i+1,0]) # toutes les arêtes sont valuées à zéro 
                edges.append([i,i+W,0]) # pour le moment
        # arêtes de la fin
        for x in range(0,W-1):
            i = (H-1)*W + x
            edges.append([i,i+1,0])
        for y in range(0,H-1):
            i = y * W + (W-1)
            edges.append([i,i+W,0])
    
    ## "8-connectivité"
    if (type == '8'):
        for y in range(0,H-1):
            for x in range(1,W-1):
                i = y * W + x
                edges.append([i,i+1,0]) # toutes les arêtes sont valuées à zéro 
                edges.append([i,i+W,0]) # pour le moment
                edges.append([i,i+W+1,0]) # NW-SE
                edges.append([i,i+W-1,0]) # NE-SW
        # arêtes verticales début et fin
        for y in range(0,H-1):
            i = y * W + (W-1)
            edges.append([i,i+W,0])
            edges.append([i,i+W-1,0])
            i = y * W
            edges.append([i,i+1,0])
            edges.append([i,i+W+1,0])
            edges.append([i,i+W,0])
        # arête horizontales fin
        for x in range(0,W-1):
            i = (H-1)*W + x
            edges.append([i,i+1,0])
        
    
    if (type == 'H'): ## horizontal adjacence
        for y in range(0,H-1):
            for x in range(0,W-1):
                i = y * W + x
                edges.append([i,i+1,0]) # arètes horizontales seulement
        # arêtes horizontales de la fin
        for x in range(0,W-1):
            i = (H-1)*W + x
            edges.append([i,i+1,0])

    if (type == 'V'): ## vertical adjacence
        for y in range(0,H-1):
            for x in range(0,W-1):
                i = y * W + x
                edges.append([i,i+W,0]) # arêtes verticales seulement
        # arêtes verticales de la fin
        for y in range(0,H-1):
            i = y * W + (W-1)
            edges.append([i,i+W,0])
            
    ### Definissez aussi les deux diagonales comme deux adjacences séparées.
    if (type == 'D1'):
        for y in range(0,H-1):
            for x in range(1,W-1):
                i = y * W + x
                edges.append([i,i+W+1,0]) # NW-SE
        # arêtes verticales début et fin
        for y in range(0,H-1):
            i = y * W
            edges.append([i,i+W+1,0])
            
        ## "8-connectivité"
    if (type == 'D2'):
        for y in range(0,H-1):
            for x in range(1,W-1):
                i = y * W + x
                edges.append([i,i+W-1,0]) # NE-SW
        # arêtes verticales début et fin
        for y in range(0,H-1):
            i = y * W + (W-1)
            edges.append([i,i+W-1,0])
    
    return(Graph(edges,nodes,W,H))