import os
from collections import defaultdict
from collections import deque
#os.chdir("C:\\Users\\maxwell\\Documents\\cis315\\asgn2")
##
def main():
    with sys.stdin as fil:
        
        def toposort(graph):
    
            from functools import reduce
            data = defaultdict(set)
            for x, y in graph.items():
                for z in y:
                    data[z[0]].add(x)
        
            # Ignore self dependencies.
            for k, v in data.items():
                v.discard(k)
            # Find all items that don't depend on anything.
            extra_items_in_deps = reduce(set.union, data.values()) - set(data.keys())
            # Add empty dependences where needed
            data.update({item:set() for item in extra_items_in_deps})
            while True:
                ordered = set(item for item, dep in data.items() if not dep)
                if not ordered:
                    break
                yield ordered
                data = {item: (dep - ordered)
                        for item, dep in data.items()
                            if item not in ordered}
            assert not data, "Cyclic dependencies exist among these items:\n%s" % '\n'.join(repr(x) for x in data.items())
        
        def longestpathDAG(graph, startnode, endnode):
            order = []
            for part in toposort(graph):
                order.extend(list(part))
            if len(graph)<len(order):
                graph[order[-1]]=[]
            LOWDIST=-99999999999999999
            dist = dict((x, LOWDIST) for x in graph.keys())
            dist[startnode] = 0
        
            comesfrom = dict()
            for node in order: # u
                for nbr, nbrdist in graph[node]:
                    if dist[nbr] < dist[node] + nbrdist:
                        dist[nbr] = dist[node] + nbrdist
                        comesfrom[nbr] = node
        
            maxpath = [endnode]
            while maxpath[-1] != startnode:
                maxpath.append(comesfrom[maxpath[-1]])
            maxpath.reverse()
        
            return dist[endnode], maxpath
        
        
        
    #file= open('samplein.py', 'r')
        
        #a=file.readlines()
        
        a=fil.readlines()
        nodes=[]
        all=[]
        agg=[]
        first=0
        count=1
        for line in a:
            stop=len(a)
            line2=line.rstrip("\n")
            nums= line2.rsplit(' ')
            n=nums[0:3]
            if len(n)==1:
                graphs=n
                count+=1
            elif len(n) == 2 and first ==1:
                print('run1')
                nodes.append(n)
                all.append(agg)
                agg=[]
                count+=1
            elif len(n) == 2:
                nodes.append(n)
                first=1
                count+=1
            elif len(n) == 3:#notworking add if  statement to look for same vertex here. 
                agg.append(n)
                if count == stop:
                    print('run2')
                    all.append(agg)
                count+=1
                
        ##all has my two graphs
        gr=[]
        c=1
        e=0
        for g in all:
            keys=[]
            values=[]
            weights=[]
            for line in g:
                vee=line
                q=deque(vee)
                key=int(q.popleft())
                keys.append(key)
                values.append(int(q.popleft()))
                weights.append(int(q.popleft()))
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
                
            gr.append(d)
        
            dist,path=longestpathDAG(gr[e],1,len(d)+1)
            e+=1
            print("Graph number is")
            print(c)
            print("longest path distance")
            print(dist)
            print("number os longest paths are")
            print(path)
            c+=1
main()
    
    
    
    
    
    
    
    





