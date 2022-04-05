from polygon_selector import new_func
from utilities import get_info
import numpy as np
import re

print("Opt to use polygon select GUI (Y/n)")
flag = input()

if flag.lower() == 'y':
    Vertices = new_func('__main__')
else:
    Vertices = []
    n = int(input("Enter number of vertices : "))
    
    # iterating till the range
    print("Enter integer vertex in counter-clockwise order, starting at the origin, in [x,y] format")
    for i in range(0, n):
        a = input()
        # delete non-numeric characters
        # result = re.sub('[^0-9]','', a)
        result = ''.join(c for c in a if c != '[' and c != ']')
        result = result.split(',')
        # put coordinates in list format
        vertex = list(result)
        # make type integer
        vertex = [int(s) for s in vertex]
        # append to list
        Vertices.append(np.array(vertex))
    Vertices = np.array(Vertices)
    print(Vertices)
get_info(Vertices)