## Python simplexe in numpy form

from __future__ import print_function

import numpy as np


def simplexit(A,b,c, init, debug=True, expectNullOptimum=False):
    """
    Implements the standard matrix form of the simplex algorithm

    Hugues Talbot 2018, from an initial version in R ca. 2009.
    """
    iter = 0
    dim=A.shape[0]
    nbvar=A.shape[1]
    lastx=0
    lastxl=0
    sol=None
    IBVmem=None # to detect cycles

    vars=np.arange(0,nbvar) # indices start at 0
    IBV=init # Initial basis vector
    while (True):
        if debug:
            print("*** Iteration: ", iter)
        NBV = np.setdiff1d(vars,IBV) # Set complement -> non basis variables
        if debug:
            print("    IBV = ", IBV)
            print("    NBV = ", NBV)

        B=A[:,IBV]
        E=A[:,NBV]
        cb = c[IBV]
        ce = c[NBV]

        if debug:
            print("    B = \n", B)
            print("    E = \n", E)

        try:
            iB = np.linalg.inv(B)
        except:
            print("B is not invertible, error")
            break

        if debug:
            print("    iB = \n", iB)

        bbar = iB.dot(b)
        if (np.min(bbar) < -1e-7):
            print("bbar is not positive, not a feasible solution")
            break

        if debug:
            print("    bbar= ", bbar)

        cebart = ce.T - cb.T.dot(iB).dot(E)

        if debug:
            print("  reduced costs", cebart)

        if (np.min(cebart) >= 0):
            print(" optimum found!")
            sol = (IBV, bbar)
            print("IBV = ", IBV)
            print("Bbar= ", bbar)
            if ((np.min(cebart) > 0) or expectNullOptimum):
                break
            if (IBVmem is None):
                IBVmem = IBV
            else:
                if (IBV == IBVmem):
                    print("Cycle detected\n")
                    break

        l = np.argmin(cebart) # may not be unique
        P = iB.dot(A[:,NBV[l]])
        if (debug):
            print("P = ", P)
        if (np.max(P) <= 0):
            print("Solution in unbounded!")
            break
        ratios = bbar/P ## elementwise division
        if (debug):
            print("Ratios = ", ratios)
        ## Ignore negative members f P
        negP = P < 0
        ratios[negP] = np.inf ## this way they will not be selected as the min
        nanP = np.isnan(ratios)
        ratios[nanP] = np.inf ## nan are eliminated as well
        if (debug):
            print("Fixed ratios = ", ratios)
        xl = np.min(ratios)
        j = np.argmin(ratios)
        lastx = xl
        lastxl = NBV[l]
        if (debug):
            print("Variable (", IBV[j],") in the basis replaced by variable (",NBV[l],")\n",sep="")
            print("xl = ",xl)

        IBV[j] = NBV[l]
        if (debug):
            print("IBV = ", IBV)

        iter += 1
        ## end while
        
    return sol

