import DBScan
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

def EuclidieanDist(X,Y):
    #print(str(X)+"-"+str(Y))
    dist = sqrt((X[0] - Y[0]) ** 2 + (X[1] - Y[1]) ** 2)
    return dist
def dataimport():
    datafile = "dataset/s1.txt"
    dtlist = []
    i=0
    with open(datafile,"r") as data:
        for l in data:
            i+=1
            if(i%2==0):
                continue
            if(i>1000):
                break
            line = l.split("   ")
            if len(line)<3:
                continue
            d2 = line[2].replace("\n","").replace(" ","")
            dtlist.append([int(line[1].replace(" ","")),int(d2)])
    return dtlist
def dataToXY(data):
    pltX = np.array(data)[:,0]
    pltY = np.array(data)[:,1]
    return pltX,pltY

def plottingInSameFigure(clusters):
    number = len(clusters)
    cmap = plt.get_cmap('gnuplot')
    colors = [cmap(i) for i in np.linspace(0, 1, number)]

    for i, color in enumerate(colors, start=1):
        if not clusters[i-1]:
            continue
        pltX,pltY = dataToXY(clusters[i-1])
        plt.plot(pltX, pltY, 'ro', color=color)
    plt.legend(loc='best')
    plt.savefig("clustered.png")
def evaluation():
    '''
    evaluate cluster method
    :return:
    '''

def __main():
    eps = 8
    minPts = 2
    # 2D data import
    #data = [[1, 1], [1, 2], [2, 1], [2, 2], [2.1, 2.1], [1.7, 1.8], [11, 11], [12, 12], [11.11, 12.3], [11.95, 13],[12, 11.3], [12.7, 11], [35, 35],[34,31],[29,36],[45,19]]
    data = dataimport()
    #data plotting
    plt.figure(0)
    pltX,pltY = dataToXY(data)
    plt.plot(pltX,pltY,'ro')
    plt.savefig("data_.png")
    x=2
    Clsturs = DBScan.apply(data,eps=175000,minPts=50)
    for c  in Clsturs:
        if not c:
            continue
        plt.figure(x-1)
        pltX,pltY = dataToXY(c)
        plt.plot(pltX,pltY,'ro')
        plt.savefig("set_"+str(x-1)+".png")

        x+=1
    print(x)
    plt.savefig("data_clusters.png")
    plottingInSameFigure(Clsturs)
    #print(Clsturs)
    #clusters on chart


__main()
