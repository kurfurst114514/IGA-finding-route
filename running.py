from algorithm import *
import tkinter

map=Map()
M=30


def func(map,M,T,ep):
    maxpath=[]
    maxfit=0
    minpathnum=0
    minfit=0
    Pathset=gene_init_group(map,M)
    Pathset=insert(Pathset,map)
    for i in range(len(Pathset)):
        Pathset[i]=delete(Pathset[i],map)
    for i in range(len(Pathset)):
        tmp=fit(Pathset[i],map)
        if(tmp>maxfit):
            maxfit=tmp
            maxpath=deepcopy(Pathset[i])
        if(tmp<minfit):
            minfit=tmp
            minpathnum=i
    for i in range(len(Pathset)):
        if(random()<clone_p(Pathset,i,map,0.02,1.5)):
            Pathset.append(deepcopy(Pathset[i]))
    Pathset=exchange(Pathset,ep)
    Pathset=variation(Pathset,0.18,map)
    for m in range(T):
        for i in range(len(Pathset)):
            tmp=fit(Pathset[i],map)
            if(tmp>maxfit):
                maxpath=deepcopy(Pathset[i])
                maxfit=tmp
                Pathset.append(maxpath)
            else:
                Pathset.append(maxpath)
                del Pathset[minpathnum]
        for i in range(len(Pathset)):
            if(random()<clone_p(Pathset,i,map,0.02,1.5)):
                Pathset.append(deepcopy(Pathset[i]))
        Pathset=exchange(Pathset,ep)
        Pathset=variation(Pathset,0.18,map)
        Pathset=choicef(Pathset,map)
    maxpath=delete(maxpath,map)
    return maxpath

def drawline(x,y,tx,ty,canvas):
        dx=tx-x
        dy=ty-y
        steps=0
        if(dx>dy):
            steps=dx
        else:
            steps=dy
        if(steps==0):
            return
        xin=dx/steps
        yin=dy/steps
        xi=x
        yi=y
        for i in range(steps):
            canvas.create_rectangle(int(xi)*20,int(yi)*20,(int(xi)+1)*20,(int(yi)+1)*20,fill="#87CEFA")
            xi=xi+xin
            yi=yi+yin
        return

window=tkinter.Tk()
window.geometry("500x500")
window.title("IGA")
canvas=tkinter.Canvas(window,bg="white",height=500,width=500)
canvas.pack()
for i in range(map.N):
    for j in range(map.N):
        if(map.map[i][j]==0):
            canvas.create_rectangle(i*20,j*20,(i+1)*20,(j+1)*20,fill="#FFDEAD")
        else:
            canvas.create_rectangle(i*20,j*20,(i+1)*20,(j+1)*20,fill="#8B4726")
window.update()
while(map.startx!=map.endx-1 or map.starty!=map.endy-1):
    path=func(map,M,100,0.8)
    tmp=path[1]
    nx=map.num_to_xy(tmp)[0]
    ny=map.num_to_xy(tmp)[1]
    ntheta=0
    if(ny-map.starty!=0):
        ntheta=math.atan((nx-map.startx)/(ny-map.starty))
    else:
        ntheta=math.pi/2
    drawline(map.startx,map.starty,nx,ny,canvas)
    map.startx=nx
    map.starty=ny
    map.theta=ntheta
    window.update()
window.mainloop()
