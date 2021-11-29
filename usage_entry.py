#Usage exampel:
import numpy as np
import utilities

if __name__ == "__main__":
    # Example 1
    # test = np.array([[1, 0],
    #                  [7, 0],
    #                  [1, 1],
    #                  [-2, 1]]
    #                 )
    # utilities.show_info(test, False)

    test = np.array([[0, 0],
                     [13, -13],
                     [13, 4],
                     [12, 5],
                     [8, 7],
                     [0, 7]])
    utilities.show_info(test, True)