




dists=[]
dists.append(dist)


for i in graphs:
    print("Graph number is")
    print(i)
    print("longest path distance")
    print(dist[1])
    print("number os longest paths are")



def readin():
    all=[]
    graphs=0
    vertedge=0
    vee=0
    key=0
    g=0
    from collections import deque

    file= open('samplein.py', 'r')

    read=1
    first =0

    keys=[]
    values=[]
    weights=[]
    for line in file:
        #print(line)
        line2=line.rstrip("\n")
        nums= line2.rsplit(' ')
        n=nums[0:3]
        if len(n)==1:
            graphs=n
        elif len(n) == 2 and first ==1:
            vertedge = n
            read=0
            break
        elif len(n) == 2:
            first=1
        elif len(n) == 3:#notworking add if  statement to look for same vertex here. 
            vee=n
            q=deque(vee)
            key=int(q.popleft())
            keys.append(key)
            values.append(int(q.popleft()))
            weights.append(int(q.popleft()))
#i want to 
    d=dict.fromkeys(keys)
    for i in range(1,len(d)+1):
        #print(i)
        lis=[]
        for j in range(len(keys)):
            #print(j)
            if i==keys[j]:
                lis.append((values[j],weights[j]))
                #if 1=1zip
                #add valuesto lis 
        #print(lis)
        d[i] = lis    
    
##

    all.append(adj)
    return keys,values,weights
                
readin()



