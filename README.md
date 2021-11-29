# Semi-toric_Packing_Capacity
Semi/toric Packing

This repo is for saving the program for calculating, and showing the packing capacity of the Semi/toric.

Intro Page:
https://math.illinois.edu/research/igl/projects/fall/2021/toric-and-semitoric-packing-capacities


## Function Usage
show_info(Vertices) is the entry function. (usage_entry.py)

By default, it shows one maximum situation. To show all possibilities, use show_info(Vertices, all = True) OR show_info(Vertices, True).

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
Notice: decimal or negative input are accepted
## Function Logics
def scale(vertices):
    Multiple each coordinate with LCM of all vertices coordinates.

def show_graph(Vertices, sl2_length, set, tittle=""):
    Get the ratio of SL2 length in packing condtion to the SL2 length of original line. Then find the all three vertices coordinates and the plot the triangular packing area.

def verifyDelzant(vert, nA, nB)
    Check whether the determinate of composed matrix has absolute value of 1.

def get_candidate(SL_length, k)
    Utilize k inequalities between lambdas and set (# of vertices - k) lambda as 0. The solve the matrix euqation to check whether there is a valid solution.




## The list of functions in utilities.py

def checkConvex(vertices)
As signature, this function is used to check whether the polygon is Convex

def scale(vertices)
If there is any decimal coordinates, scale the whole polygon into integer coordinates

def show_graph(Vertices, sl2_length, set, tittle="")
Generate the graph for the packing sitation. Third parameter is optional.

def verifyDelzant(vert, nA, nB)
As signature, check if the corner is Delzant corner

def getSL(vert, nVert)
As signature, get the size of SL2 length

def get_edges(vertices)
As signature, get the vector form of edges

def get_candidate(SL_length, k)
Using permuation to calculate all possible packing conditions, "k" represent the number of used inequality between lamdas.

def magnitude(Vertex)
Get the magniture of current packing area.

def get_vertex(SL_length)
Get all possible packing conditions by calling get_candidate function. Then sort all packing candidate by their own magnitude.

def filter(vertex, SL2)
Return True is the packing is resilient with SL2 length condition, otherwise, return False.

def parse(SL2_lengths)
Return all possible packing conditions which share the same maximum pakcing magnitude.

def show_info(Vertices)
Integerate all prompt messages and use all helper functions above for final information representation. 


![image](https://github.com/CoulsonZhang/Semi-toric_Packing_Capacity/blob/main/Image/UIUC_logo.png)
