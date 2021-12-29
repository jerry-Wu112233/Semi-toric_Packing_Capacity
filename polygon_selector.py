"""
================
Polygon Selector
================

Shows how one can select indices of a polygon interactively.
"""

import numpy as np
import math

from matplotlib.widgets import PolygonSelector
from matplotlib.path import Path
from numpy.lib.function_base import delete


def new_func(__name__):
    class SelectFromCollection:
        """
    Select indices from a matplotlib collection using `PolygonSelector`.
    Selected indices are saved in the `ind` attribute. This tool fades out the
    points that are not part of the selection (i.e., reduces their alpha
    values). If your collection has alpha < 1, this tool will permanently
    alter the alpha values.
    Note that this tool selects collection objects based on their *origins*
    (i.e., `offsets`).
    Parameters
    ----------
    ax : `~matplotlib.axes.Axes`
        Axes to interact with.
    collection : `matplotlib.collections.Collection` subclass
        Collection you want to select from.
    alpha_other : 0 <= float <= 1
        To highlight a selection, this tool sets all selected points to an
        alpha value of 1 and non-selected points to *alpha_other*.
    """

        def __init__(self, ax, collection, alpha_other=0.3):
            self.canvas = ax.figure.canvas
            self.collection = collection
            self.alpha_other = alpha_other

            self.xys = collection.get_offsets()
            self.Npts = len(self.xys)

        # Ensure that we have separate colors for each object
            self.fc = collection.get_facecolors()
            if len(self.fc) == 0:
                raise ValueError('Collection must have a facecolor')
            elif len(self.fc) == 1:
                self.fc = np.tile(self.fc, (self.Npts, 1))

            self.poly = PolygonSelector(ax, self.onselect)
            self.ind = []

        def onselect(self, verts):
            path = Path(verts)
            self.ind = np.nonzero(path.contains_points(self.xys))[0]
            self.fc[:, -1] = self.alpha_other
            self.fc[self.ind, -1] = 1
            self.collection.set_facecolors(self.fc)
            self.canvas.draw_idle()

        def disconnect(self):
            self.poly.disconnect_events()
            self.fc[:, -1] = 1
            self.collection.set_facecolors(self.fc)
            self.canvas.draw_idle()

    origin = [0, 0]
    refvec = [0, 1]
# function adapted from from https://stackoverflow.com/a/41856340
    def counterclockwise(point):
    # Vector between point and the origin: v = p - o
        vector = [point[0]-origin[0], point[1]-origin[1]]
    # Length of vector: ||v||
        lenvector = math.hypot(vector[0], vector[1])
    # If length is zero there is no angle
        if lenvector == 0:
            return -math.pi, 0
    # Normalize vector: v/||v||
        normalized = [vector[0]/lenvector, vector[1]/lenvector]
        dotprod  = normalized[0]*refvec[0] + normalized[1]*refvec[1]     # x1*x2 + y1*y2
        diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]     # x1*y2 - y1*x2
        angle = math.atan2(diffprod, dotprod)
    # Negative angles represent counter-clockwise angles so we need to subtract them 
    # from 2*pi (360 degrees)
        if angle < 0:
            return 2*math.pi+angle, lenvector
    # I return first the angle because that's the primary sorting criterium
    # but if two vectors have the same angle then the shorter distance should come first.
    
    # return negative angle for counterclockwise orientation
        return -angle, lenvector

    if __name__ == '__main__':
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        grid_size = 5
        grid_x = np.tile(np.arange(grid_size), grid_size)
        grid_y = np.repeat(np.arange(grid_size), grid_size)
        pts = ax.scatter(grid_x, grid_y)

        selector = SelectFromCollection(ax, pts)

        print("Select points in the figure by enclosing them within a polygon.")
        print("Press the 'esc' key to start a new polygon.")
        print("Try holding the 'shift' key to move all of the vertices.")
        print("Try holding the 'ctrl' key to move a single vertex.")

        plt.show()

        selector.disconnect()

    # sort the vertices in counterclockwise order
    
        # not all of these points are vertices
        vert = np.array(selector.xys[selector.ind])
        vert = np.array(sorted(vert, key=counterclockwise))
                
    # After figure is closed print the coordinates of the selected points
        print('\nSelected points:')
        # print(vert[:, 0], vert[:, 1])
        # go through vert[:, 0] and vert[:, 1]
        
        # delete all middle elements
        to_delete = []
        n = vert.shape[0]
        for i in range(n):
            for k in range(2):
                if int(vert[i,k]) == int(vert[(i+1) % n, k]) == int(vert[i - 1, k]):
                    to_delete.append(i)
        vert = np.delete(vert, to_delete, axis=0)
        print(vert)

#############################################################################
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.widgets.PolygonSelector`
    #    - `matplotlib.path.Path`

    return vert
