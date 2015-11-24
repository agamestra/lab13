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

    def determinant (self):
        pass

    def __eq__(self, other):
        flag=0
        for a in range (m):
            for b in range (n):
                if Mat[a,b]:
                    pass

    def get(self, i, j):
        return Mat(i,j)

    def get_m(self):
        return self.m

    def get_n(self):
        return self.n

    def get_size(self):
        pass

    def invert (self):
        pass

    def __mul__(self, other):
        pass

    def set(self, i, j, value):
        Mat[i,j]=value

    def __sub__(self, other):
        pass

    def transpose (self):
        pass

    def __truediv__(self, other):
        pass
    