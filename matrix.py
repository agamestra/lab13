class Matrix:


    def __init__(self, m, n=None):
        self.m=m
        self.n=n
        if n==None:
            Mat=int([0])*m
        else:
            Mat=int([0])*m
            for a in range (m):
                Mat[a]=[0]*n

    def __add__(self, other):

        pass

    def get(self, i, j):
        return Mat(i,j)

    def set(self, i, j, value):
        Mat[i,j]=value


