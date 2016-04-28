import os
os.chdir("C:\\Users\\maxwell\\Documents\\cis315\\asgn2")
##
import sys
with sys.stdin as fil:
    for line in fil:
        nums= line.split(' ')
##

graphs=0
vertedge=0
vee=0
key=0
g=0
keys=[]
values=[]
    
from collections import deque
file= open('samplein.py', 'r')
read=1
first =0
while(read==1):
    for line in file:
        #print(line)
        line2=line.rstrip("\n")
        nums= line2.rsplit(' ')
        n=nums[0:3]
        if len(n)==1:
            graphs=2
        elif len(n) == 2 and first ==1:
            vertedge = n
            read=0
            break
        elif len(n) == 2:
            first=1
        elif len(n) == 3:#notworking add if  statement to look for same vertex here. 
            vee=n
            q=deque(vee)
            key=q.popleft()
            keys.append(key)
            values.append(q)
#i want to 

def paths(keys,values):
    d=dict.fromkeys(keys)
    for i in range(1,len(d)+1):
        #print(i)
        lis=deque([])
        for j in range(len(keys)):
            #print(j)
            if str(i)==keys[j]:
                lis+=values[j]
                #if 1=1zip
                #add valuesto lis 
        #print(lis)
        d[str(i)] = lis    
        
    ##
    adj=d
    def find_all_paths(graph, start, end, path=[]):
            path = path + [start]
            if start == end:
                return [path]
            if graph.get(start) == None:
                return []
            paths = []
            for node in graph[start]:
                if node not in path:
                    newpaths = find_all_paths(graph, node, end, path)
                    for newpath in newpaths:
                        paths.append(newpath)
            return paths
    all=find_all_paths(adj,'1','10')
        
    def find_longest_path(graph, start, end, path=[]):
            path = path + [start]
            if start == end:
                return path
            if graph.get(start) == None:
                return None
            longest = None
            for node in graph[start]:
                if node not in path:
                    newpath = find_longest_path(graph, node, end, path)
                    if newpath:
                        if not longest or len(newpath) > len(longest):
                            longest = newpath
            return longest
    
    p=find_longest_path(adj,'1','10')
    
    n=len(p)#longest
    longest=[]
    
    for i in all:
        if len(i) == n:
            longest.append(i)
    second=longest.copy()
    duplicates=[]
    for i in range(0,len(second)//2):
        #print(i)
        longest.remove(second[i])
        if second[i] in longest and second[i] not in duplicates:
            duplicates.append(second[i])
    
    def remove_values_from_list(the_list, val):
        return [value for value in the_list if value != val]
    for word in duplicates:
        second = remove_values_from_list(second,word)
    
    uniquepaths=len(second)
    
    print(n)
    print(uniquepaths)
paths(keys,values)