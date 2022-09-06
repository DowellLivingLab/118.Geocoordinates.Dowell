import numpy as np
from math import sqrt
import pandas as pd
from IPython.display import HTML
import matplotlib.pyplot as plt
import base64
import io

import ctypes
import glob

def inscribe(radius,length,width,layout):
        # print("Successfull 0\n")

        # find the shared library, the path depends on the platform and Python version
        libfile = glob.glob('build/*/algorithm*.so')[0]
        # print("Successfull 1\n")

        # 1. open the shared library
        mylib = ctypes.CDLL(libfile)

        mylib.inscribe.restype = ctypes.POINTER(ctypes.c_double)
        mylib.inscribe.argtypes = [ctypes.c_float, ctypes.c_int, ctypes.c_int]

        result = mylib.inscribe(radius, length, width)
        # print("Successfull 2\n")
        height = round(radius*sqrt(3),3)

        mylib.seq1Count.restype = ctypes.POINTER(ctypes.c_float)
        mylib.seq1Count.argtypes = [ctypes.c_float, ctypes.c_int, ctypes.c_float]
        mylib.seq2Count.restype = ctypes.POINTER(ctypes.c_float)
        mylib.seq2Count.argtypes = [ctypes.c_float, ctypes.c_int, ctypes.c_float]

        a = mylib.seq1Count(0.0,length,height)
        b = mylib.seq2Count(0.0,width,radius)

        print("Getting Points from C++ Done\n")

        aList = []
        bList = []
        print("a = ", a[0])
        print("b = ", b[0])
        for i in range (1,int(a[0]) + 1):
            aList.append(round(a[i],3))
        for i in range (1, int(b[0]) + 1):
            bList.append(round(b[i],3))

        print("Converting of a and b into List Done\n")

        # print(aList)
        # print(bList)


        final_df = pd.DataFrame(columns=aList,index=bList)
        final_df.replace(to_replace=np.NaN,value="",inplace=True)

        print("DataFrame columns and index set\n")

        # print(final_df)
        # print("\nPrinting\n")
        # for i in range(1, ( (2 * (int(result[0]))) + 1 )):
        #     print(round(result[i], 3))
        for i in range(1, ( (2 * (int(result[0]))) + 1 ), 2):
            final_df.at[round(result[i+1], 3), round(result[i], 3)] = [round(result[i+1], 3), round(result[i],3)]

        print("DataFrame all points inserted\n")
        # print(final_df)
        #print("No. of circles that can be inscribed in "+str(input_length)+"X"+str(input_width)+" canvas:",len(flattened_list))
        ts = HTML(final_df.to_html())

        print("HTML conversion DONE\n")

        layout = layout
        img_data = ""
        if layout == "y" :

                    #separating the x and y coordinates in different lists
                    xlist=[]
                    for i in range(1, ( (2 * (int(result[0]))) + 1 ), 2):
                        xlist.append(result[i])

                    ylist=[]
                    for i in range(2, ( (2 * (int(result[0]))) + 1 ), 2):
                        ylist.append(result[i])
                    # Enter x and y coordinates of points
                    xs = xlist
                    ys = ylist
                    x_bound = (length/2)
                    y_bound = width/2


                    # Select length of axes and the space between tick labels
                    xmin, xmax, ymin, ymax = -(x_bound+1), x_bound+1, -y_bound, y_bound
                    ticks_frequency = 1

                    # Open a figure
                    fig, ax = plt.subplots(figsize=(150,150))

                    # Draw circles with centre at (x,y) and given radius
                    for i in range(len(xs)):
                        for j in range(len(ys)):
                            if i==j:
                                circle = plt.Circle((xs[i],ys[j]),radius,color='#00008B',linewidth=1,fill=False)
                                ax.add_patch(circle)

                    # Plot the (x,y) points to mark the center of the circles
                    ax.scatter(xs, ys,c='#FF4500')

                    #Set the length and width of the figure
                    fig.set_figwidth(90)
                    fig.set_figheight(90)

                    # Set backgroung color for the figure
                    ax.set_facecolor('#f1ef8e')

                    # Set identical scales for both axes
                    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

                    # Set bottom and left spines as x and y axes of coordinate system
                    ax.spines['bottom'].set_position('zero')
                    ax.spines['left'].set_position('zero')

                    # Draw lines to indicate the boundaries of the canvas
                    plt.vlines(x = max(xs), ymin = -(y_bound), ymax = y_bound, colors = 'purple',label = 'vline_multiple - full height',linestyle = 'dashed')
                    plt.vlines(x = -max(xs), ymin = -(y_bound) , ymax = y_bound, colors = 'purple',label = 'vline_multiple - full height',linestyle = 'dashed')
                    plt.hlines(y = y_bound, xmin = max(xs), xmax = -max(xs), colors = 'purple',label = 'vline_multiple - full height',linestyle = 'dashed')
                    plt.hlines(y = -(y_bound), xmin = max(xs), xmax = -max(xs), colors = 'purple',label = 'vline_multiple - full height',linestyle = 'dashed')


                    # Remove top and right spines
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)

                    # Create 'x','y' and 'O' labels
                    ax.set_xlabel('X', size=50, labelpad=-24, x=1.03)
                    ax.set_ylabel('Y', size=50, labelpad=-21, y=1.02, rotation=0)
                    plt.text(0.499, 0.499, r"O", ha='right', va='top',
                    transform=ax.transAxes,
                         horizontalalignment='center', fontsize=20)

                    # Create custom major ticks to determine position of tick labels
                    x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
                    y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
                    ax.set_xticks(x_ticks[x_ticks != 0])
                    ax.set_yticks(y_ticks[y_ticks != 0])

                    # Create minor ticks placed at each integer to enable drawing of minor grid
                    ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
                    ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

                    # Draw major and minor grid lines
                    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

                    # Draw arrows
                    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
                    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
                    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

                    plt.title("IN-CIRCLES PLOTTED IN A CARTESIAN PLANE",fontsize=25,y=-0.02)

                    #plt.show()
                    sio = io.BytesIO()
                    fig.savefig(sio)
                    sio.seek(0)
                    img_data = base64.b64encode(sio.read()).decode('ascii')
        elif layout == "n" :
            print("Layout not required")
        else:
            print("You can enter either y or n")

        #graph = mpld3.display(fig=None, closefig=True, local=False)
        return img_data,ts,int(result[0])
