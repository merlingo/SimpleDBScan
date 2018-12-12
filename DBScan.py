from math import sqrt


def getLabel(p,listOfClusters):
    '''
    return the label of p, answer the question whether the point p belongs to which cluster

    :param p: point
    :return: (int) cluster label, if Noise then return -1, if no cluster return None
    '''
    c=0
    for cluster in listOfClusters:
        if(tuple(p) in cluster):
            if(c==0):
                return "Noise"
            return c
        c+=1
    return None
def setLabel(p,C,listOfClusters):
    '''
    set p into cluster C
    :param p:
    :param C:
    :return:
    '''
    e=0 #if it is noise
    if C is not "Noise":
        e=C
    print(str(p)+" to "+str(e))
    listOfClusters[e].add(tuple(p))
def rangeQuery(data,distFunc,q,eps):
    '''
    for getting set whose elements are in range calculated with distFunc
    :param data:
    :param distFunc:
    :param p:
    :param eps:
    :return: a set
    '''
    neighbourSet = set()
    for p in data:
        if(distFunc(q,p)<eps):
            neighbourSet.add(tuple(p))
    return neighbourSet
def EuclidieanDist(X,Y):
    dist = sqrt((X[0] - Y[0]) ** 2 + (X[1] - Y[1]) ** 2)
    print(str(X)+"-"+str(Y)+":"+str(dist))
    return dist
def apply(data,distFunc=EuclidieanDist,eps=8,minPts=2):
    '''
    apply DBScan cluster algorithm
    :param data:
    :param distFunc:
    :param eps:
    :param minPts:
    :return: no return value
    '''
    C=0
    listOfClusters = [set()]
    for p in data:
        if getLabel(p,listOfClusters) is not None:
            continue
        N = rangeQuery(data,distFunc,p,eps) #N is set of data in range
        if (len(N)<minPts):
            setLabel(p,"Noise",listOfClusters)
            continue
        C+=1
        listOfClusters.append(set())
        setLabel(p,C,listOfClusters)
        S = N.difference(set([tuple(p)]))
        for q in S:
            if getLabel(q,listOfClusters)=="Noise":
                setLabel(p, C,listOfClusters)
            elif getLabel(q,listOfClusters) is not None:
                continue
            setLabel(q,C,listOfClusters)
            Nq = rangeQuery(data,distFunc,p,eps)
            if(len(Nq)>= minPts):
                S=S.union(Nq)
    return clusters(listOfClusters)

def clusters(loc):
    l=[]
    for cs in loc:
        c=[]
        for t in cs:
            c.append([t[0],t[1]])
        l.append(c)

    return l

