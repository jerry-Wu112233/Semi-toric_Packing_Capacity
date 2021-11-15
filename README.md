# Semi-toric_Packing_Capacity
Semi/toric Packing

This repo is for saving the program for calculating, and showing the packing capacity of the Semi/toric.

Intro Page:
https://math.illinois.edu/research/igl/projects/fall/2021/toric-and-semitoric-packing-capacities

## The list of functions in utilities.py

def checkConvex(vertices)

def scale(vertices)

def show_graph(Vertices, sl2_length, first, tittle="")

def verifyDelzant(vert, nA, nB)

def getSL(vert, nVert)

def get_edges(vertices)

def get_candidate(SL_length, k)

def get_vertex(SL_length)

def magnitude(Vertex)

def filter(vertex, SL2)

def parse(SL2_lengths)

def show_info(Vertices)

## Function Usage
show_info(Vertices) is the entry of the program.

Input: 2D np array for list of vertices in Counterclockwise order
show_info(Input) will display all related information regarding the input list of vertices

For example, the 2D polygon with vertices: (0,0); (13,-13); (13,4); (12,5); (8,7); (0,7) will be in the form of:
```
vertices = np.array([[0,0],
                 [13,-13],
                 [13,4],
                 [12,5],
                 [8,7],
                 [0,7]])
```


## Function Logics

