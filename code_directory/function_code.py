import numpy as np
import math
from math import sqrt
import pandas as pd
import itertools
from IPython.display import HTML
import matplotlib.pyplot as plt,mpld3
import base64
import io

def inscribe(radius,length,width):

            #hyp = 2*radius
        height = round(radius*sqrt(3),3)

                #iterations for x coordinates

        def seq1(start,length,step):
                y = []
                x = []
                iterations = int(10*length)
                i = 0
                count = start


                while i < iterations:
                    y.append(round(count,3))
                    if i>0:
                        x.append(round(-count,3))
                    if i != iterations:
                        count += step
                    i += 1
                    if count>((length/2)+step):
                        print("Boundary limit for X exceeded at "+str(i)+"th iterations")
                        break

                w =  list(reversed(x))
                w.extend(y)

                x_num = len(w)

                print("Total no. of X-coordinates: ",x_num)

                return w

        a = seq1(start = 0, length = length, step = height)


            #iterations for y coordinates

        def seq2(start, width, step):
                y = []
                x = []
                iterations = 10*width
                i = 0
                count = start

                while i < iterations:
                    y.append(round(count,3))
                    if i>0:
                        x.append(round(-count,3))
                    if i != iterations:
                        count += step
                    i += 1
                    if count>(width/2):
                        #print("Boundary limit for Y exceeded at "+str(i)+"th"+" iteration")
                        break

                w = list(reversed(y))
                w.extend(x)

                y_num = len(w)
                print("Total no. of Y-coordinates: ",y_num)

                return w

        b = seq2(start = 0, width = width, step = radius)


            #preparing the dataframe of the coordinates

        df = pd.DataFrame(columns=a,index=b)
        df.replace(to_replace=np.NaN,value="",inplace=True)
        df1 = df.copy() #changes in df1 will not effect in df


            #getting the odd and even indexing value of index seperating b into even indexing and odd indexing of b

        for i in b:
            for j in a:
                df.at[i,j]=[i,j]

        odd_ind = []
        even_ind = []
        for i in range(0, len(b)):
            if i % 2==0:
                even_ind.append(b[i])
            else :
                odd_ind.append(b[i])


            #getting the odd and even columns value of index seperating a into even columns and odd columns  of a

        odd_col = []
        even_col = []
        for i in range(0, len(a)):
            if i % 2==0:
                   even_col.append(a[i])
            else :
                odd_col.append(a[i])


            # for placing the even columns

        for i in even_ind:
            for j in even_col:
                df1.at[i,j]=(j,i)

            # for placing the odd columns

        for i in odd_ind:
            for j in odd_col:
                df1.at[i,j]=(j,i)


            #counting the number of circles
        final_df = df1
        arr = df1.to_numpy()
        list1 = arr.tolist()

        dd=[]
        for i in range(len(list1)):
            dd.append(list(filter(lambda a: a != '', list1[i])))

        who=[]
        for i in range(len(dd)):
             who.append(dd[i])

        chain_object = itertools.chain.from_iterable(dd)
        flattened_list = list(chain_object)
        num = len(flattened_list)
        #print("No. of circles that can be inscribed in "+str(input_length)+"X"+str(input_width)+" canvas:",len(flattened_list))
        ts = HTML(final_df.to_html())

        #separating the x and y coordinates in different lists
        xlist=[]
        for i in dd:
            for j in i:
                xlist.append(j[0])

        ylist=[]
        for i in dd:
            for j in i:
                ylist.append(j[1])
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

        #graph = mpld3.display(fig=None, closefig=True, local=False)
        return img_data,ts,num
