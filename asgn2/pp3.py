import fileinput
import os
import math
import copy
#os.chdir("C:\\Users\maxwell\Documents\cis410")

def readinput():
    b=[]
    for line in fileinput.input():
        b.append(line)
    return b

def gettest():
    b=[]
    with open('test.txt', 'r') as file:
        for line in file:
            b.append(line)
    return b


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
        self.cacheable = self.misses = self.noncacheable = 0
    def __call__(self, *args, **kwds):
        if not kwds:
            self.cacheable += 1
            try: return self.memo[args]
            except KeyError:
                self.misses += 1
                self.memo[args] = self.fn(*args)
                return self.memo[args]
            except TypeError: self.cacheable -= 1
        self.noncacheable += 1
        return self.fn(*args, **kwds)
        
def printtt(e1,e2):
    def prettyPrint(text,n,M):
        #q=e[2]
        q=text
        Ls=q.split()
        l=[len(Ls[i]) for i in range(len(Ls))]
        n=len(l)
        words=Ls
        
        ex=[[0 for row in range(0,n)] for i in range(0,n)]
        lc=[[0 for row in range(0,n)] for i in range(0,n)]
        c = [0 for row in range(0,n+1)]
        p = [0 for row in range(0,n)]
        
        #for i in lc:
            #print(i)
        inf=100000000
        for i in range(0,n):
            #print(i)
            ex[i][i] = M - l[i]
            for j in range(i+1,n):
                ex[i][j] = ex[i][j-1] - l[j] - 1
                
        minima = [0] + [10 ** 20] * n
        breaks = [0] * n
        for j in range(n):
            i = j
            while i >= 0:
                if ex[i][j] < 0:
                    cost = 10 ** 10
                else:
                    cost = minima[i] + ex[i][j] ** 3
                if minima[j + 1] > cost:
                    minima[j + 1] = cost
                    breaks[j] = i
                i -= 1
        lines = []
        j = n
        while j > 0:
            i = breaks[j - 1]
            lines.append(' '.join(words[i:j]))
            j = i
        lines.reverse()     
        print(minima[breaks[-1]])
        print(lines)
        

    M=int(e1)
    q=e2
    Ls=q.split()
    l=[len(Ls[i]) for i in range(len(Ls))]
    n=len(l)
    prettyPrint= Memoize(prettyPrint)
    prettyPrint(e2,n,M)



f=readinput()
#f=readinput()

e=[ f[i].strip('\n') for i in range(len(f))]
paras=e[0]
e.remove(paras)

for i in range(int(paras)):
    e1 = e.pop(0)
    e2=  e.pop(0)
    printtt(int(e1),e2)



            
            
            
            
            
            
            
            
            
            
            
            
            
        
