'''
    methods for converting from (e1, e2) to an ellipse

'''
import math
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Ellipse


def atanThetaDegrees(e1, e2) :
    return math.degrees(np.arctan2(e2,e1) * .5)

def acosThetaDegrees(e1, e2) :
    e = np.sqrt(e1*e1 + e2*e2)
    return math.degrees(np.arccos(e1/e) * .5)

def asinThetaDegrees(e1, e2) :
    e = np.sqrt(e1*e1 + e2*e2)
    return math.degrees(np.arcsin(e2/e) * .5)

def computeTheta(e1, e2) :
    atan2Theta = atanThetaDegrees(e1, e2)
    return atan2Theta if atan2Theta > 0 else (atan2Theta + 180)

def createEllipse(x, y, e1, e2, factor = None):
    factor = factor if factor else 1
    e = np.sqrt(e1*e1 + e2*e2)
    a = 1 / (1-e) # major axis
    b = 1 / (1+e) # minor axis
    theta = computeTheta(e1, e2)
    return Ellipse((x,y), factor * (a * np.cos(math.radians(theta))), factor * (a * np.sin(math.radians(theta))), theta)

def genPlot(skydf, sizeFactor = None):
        if skydf.size < 1 : return

        sizeFactor = sizeFactor if sizeFactor else 1

        fig, ax = plt.subplots()
        ax.set_ylim(4200.0, 0.0)
        ax.set_xlim(0.0, 4200.0)
        ax.xaxis.tick_top()
        for i in skydf.index :
            x = skydf.loc[i, "x"]
            y = skydf.loc[i, "y"]
            e1 = skydf.loc[i, "e1"]
            e2 = skydf.loc[i, "e2"]
            ax.add_artist(createEllipse(x, y, e1, e2, sizeFactor))
            
        return fig
