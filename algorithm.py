from copy import deepcopy
import math
from operator import truediv
from random import *


class Map:
    map=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    startx=0
    starty=0
    endx=len(map)
    endy=len(map[0])
    theta=0
    N=len(map)
    def xy_to_num(self,x,y):
        return x+y*self.N

    def num_to_xy(self,num):
        point=[0,0]
        point[0]=num%self.N   #x
        point[1]=int(num/self.N)   #y
        return point

    def if_success(self,x,y,tx,ty):
        if(self.map[tx][ty]==1):
            return False
        dx=tx-x
        dy=ty-y
        steps=0
        if(dx>dy):   #选择最大底边
            steps=dx
        else:
            steps=dy
        if(steps==0):   #当底边为零（两节点相同）时直接返回真
            return True
        xin=dx/steps
        yin=dy/steps
        xi=x
        yi=y
        for i in range(steps):
            if(self.map[int(xi)][int(yi)]==1):  #若连线之间经过障碍物返回假
                return False
            else:
                xi=xi+xin   #x，y递增
                yi=yi+yin
        return True

    def count_box(self,x,y,tx,ty):
        if(self.map[tx][ty]==1):
            return 0
        dx=tx-x
        dy=ty-y
        steps=0
        if(dx>dy):   #选择最大底边
            steps=dx
        else:
            steps=dy
        if(steps==0):   #当底边为零（两节点相同）时直接返回真
            return 0
        xin=dx/steps
        yin=dy/steps
        xi=x
        yi=y
        res=0
        for i in range(steps):
            if(self.map[int(xi)][int(yi)]==1):  #若连线之间经过障碍物返回假
                return 0
            else:
                xi=xi+xin   #x，y递增
                yi=yi+yin
                res+=1
        return res

    
def gene_init_group(map,M):
    Pathset=[]
    for i in range(M):
        path=[]
        path.append(map.xy_to_num(map.startx,map.starty))
        x=map.startx
        y=map.starty
        while(math.fabs(x-map.endx)>1 or math.fabs(y-map.endy)>1):
            tx=int(random()*(map.endx-x)+x)
            ty=int(random()*(map.endy-y)+y)
            if(tx==x and ty==y):
                continue
            flag=map.if_success(x,y,tx,ty)
            if(flag):
                path.append(map.xy_to_num(tx,ty))
                x=tx
                y=ty
        Pathset.append(path)
    return Pathset

def fit(path,map):
    f1p=0
    n=0
    for i in range(0,len(path)-1):
        num=path[i]
        point=map.num_to_xy(num)
        nnum=path[i+1]
        npoint=map.num_to_xy(nnum)
        f1p=f1p+math.sqrt(math.pow(point[0]-npoint[0],2)+math.pow(point[1]-npoint[1],2))
        n+=map.count_box(point[0],point[1],npoint[0],npoint[1])
    res=1/(1+1/(math.sqrt(n-1))*f1p)
    return res

def choicef(Pathset,map):
    sumf=0
    for i in range(len(Pathset)):
        sumf=sumf+fit(Pathset[i],map)
    nextnum=0
    Mp=len(Pathset)
    nextlist=[]
    listdic=dict()
    for i in range(len(Pathset)):
        ni=(Mp*fit(Pathset[i],map))/sumf
        #nextlist.append(ni-int(ni))
        listdic[ni-int(ni)]=i
        nextnum+=int(ni)
    #nextlist.sort(reverse=True)
    nextlist = sorted(listdic.items(),  key=lambda d: d[1], reverse=True)
    newPathset=[]
    for i in nextlist:
        newPathset.append(Pathset[i[1]])
    return newPathset

def exchange(Pathset,ep):
    dict={}
    for i in range(len(Pathset)):
        for j in range(1,len(Pathset[i])-1):
            if(Pathset[i][j] in dict):
                if(random()>ep):
                    continue
                ex1=dict[Pathset[i][j]]
                ex2=i
                samenode=Pathset[i][j]
                changedpath1=[]
                changedpath2=[]
                flag=False
                for m in range(len(Pathset[ex1])):
                    if(Pathset[ex1][m]!=samenode):
                        if(not flag):
                            changedpath1.append(Pathset[ex1][m])
                    else:
                        changedpath1.append(samenode)
                        flag=True
                for m in range(len(Pathset[ex2])):
                    if(Pathset[ex2][m]!=samenode):
                        if(not flag):
                            changedpath1.append(Pathset[ex2][m])
                    else:
                        #changedpath1.append(samenode)
                        flag=False
                for m in range(len(Pathset[ex2])):
                    if(Pathset[ex2][m]!=samenode):
                        if(not flag):
                            changedpath2.append(Pathset[ex2][m])
                    else:
                        changedpath2.append(samenode)
                        flag=True
                for m in range(len(Pathset[ex1])):
                    if(Pathset[ex1][m]!=samenode):
                        if(not flag):
                            changedpath2.append(Pathset[ex1][m])
                    else:
                        #changedpath2.append(samenode)
                        flag=False
                Pathset[ex1]=changedpath1
                Pathset[ex2]=changedpath2
                for k in range(len(Pathset[ex1])):
                    dict[Pathset[ex1][k]]=ex1
                for k in range(len(Pathset[ex2])):
                    dict[Pathset[ex2][k]]=ex2
                break
            else:
                dict[Pathset[i][j]]=i
    return Pathset

def insert(Pathset,map):
    for i in range(len(Pathset)):
        j=0
        while(j<len(Pathset[i])-1):
        #for j in range(0,len(Pathset[i])-1):
            xi=map.num_to_xy(Pathset[i][j])[0]
            yi=map.num_to_xy(Pathset[i][j])[1]
            xip1=map.num_to_xy(Pathset[i][j+1])[0]
            yip1=map.num_to_xy(Pathset[i][j+1])[1]
            delta=max(math.fabs(xip1-xi),math.fabs(yip1-yi))
            if(delta>1):
                nxi=int(round((xi+xip1)/2,0))
                nyi=int(round((yi+yip1)/2,0))
                swit=0
                while(map.map[nxi][nyi]==1):
                    if(nxi>0 and map.map[nxi-1][nyi]==0 and map.xy_to_num(nxi-1,nyi)!=Pathset[i][j] and map.xy_to_num(nxi-1,nyi)!=Pathset[i][j+1]):
                        nxi-=1
                    elif(nyi>0 and map.map[nxi][nyi-1]==0 and map.xy_to_num(nxi,nyi-1)!=Pathset[i][j] and map.xy_to_num(nxi,nyi-1)!=Pathset[i][j+1]):
                        nyi-=1
                    elif(nxi<len(Pathset) and map.map[nxi+1][nyi]==0 and map.xy_to_num(nxi+1,nyi)!=Pathset[i][j] and map.xy_to_num(nxi+1,nyi)!=Pathset[i][j+1]):
                        nxi+=1
                    elif(nyi<len(Pathset[0]) and map.map[nxi][nyi+1]==0 and map.xy_to_num(nxi+1,nyi)!=Pathset[i][j] and map.xy_to_num(nxi+1,nyi)!=Pathset[i][j+1]):
                        nyi+=1
                    else:
                        delta=1
                        break
                n=map.xy_to_num(nxi,nyi)
                Pathset[i].insert(j+1,n)
                j-=1
            j+=1
    return Pathset
                
def variation(Pathset,p,map):   #暂时使用4突变
    for i in range(len(Pathset)):
        for j in range(1,len(Pathset[i])-1):
            if(random()<p):
                x=map.num_to_xy(Pathset[i][j])[0]
                y=map.num_to_xy(Pathset[i][j])[1]
                varfit=fit(Pathset[i],map)
                if(x>0 and map.map[x-1][y]==0):
                    tmpath=deepcopy(Pathset[i])
                    tmpath[j]=map.xy_to_num(x-1,y)
                    if(fit(tmpath,map)>varfit):
                        Pathset[i][j]=map.xy_to_num(x-1,y)
                elif(y<map.N-1 and map.map[x][y+1]==0):
                    tmpath=deepcopy(Pathset[i])
                    tmpath[j]=map.xy_to_num(x,y+1)
                    if(fit(tmpath,map)>varfit):
                        Pathset[i][j]=map.xy_to_num(x,y+1)
                elif(x<map.N-1 and map.map[x+1][y]==0):
                    tmpath=deepcopy(Pathset[i])
                    tmpath[j]=map.xy_to_num(x+1,y)
                    if(fit(tmpath,map)>varfit):
                        Pathset[i][j]=map.xy_to_num(x+1,y)
                elif(y>0 and map.map[x][y-1]==0):
                    tmpath=deepcopy(Pathset[i])
                    tmpath[j]=map.xy_to_num(x,y-1)
                    if(fit(tmpath,map)>varfit):
                        Pathset[i][j]=map.xy_to_num(x,y-1)
    return Pathset

def delete(path,map):
    npath=[]
    for j in range(0,len(path)):
        reverj=len(path)-j-1
        x=map.num_to_xy(path[reverj])[0]
        y=map.num_to_xy(path[reverj])[1]
        if(not map.if_success(map.startx,map.starty,x,y)):
            npath.append(path[reverj])
        else:
            npath.append(path[reverj])
            break
    npath.append(path[0])
    npath.reverse()
    return npath

def genius_select(Pathset,ngpath,map):
    if(ngpath!=[]):
        A=fit(ngpath,map)
    else:
        A=0
    res=ngpath
    for i in range(len(Pathset)):
        tmp=fit(Pathset[i],map)
        if(tmp>A):
            res=deepcopy(Pathset[i])
            A=tmp
    return res
    
def concent_func(Pathset,path,map,ep):
    ck=0
    fv=fit(path,map)
    for i in range(len(Pathset)):
        qs=fv/fit(Pathset[i],map)
        if(qs>=1-ep and qs<=1+ep):
            ck+=1
    return ck

def reproduction(Pathset,path,map,ep,beta):
    res=0
    res=fit(path,map)/math.pow(concent_func(Pathset,path,map,ep),beta)
    return res

def clone_p(Pathset,k,map,ep,beta):
    ek=reproduction(Pathset,Pathset[k],map,ep,beta)
    sumei=0
    for i in range(len(Pathset)):
        sumei+=reproduction(Pathset,Pathset[i],map,ep,beta)
    return ek/sumei