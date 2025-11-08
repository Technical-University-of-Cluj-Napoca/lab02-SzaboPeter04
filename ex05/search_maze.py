import sys
from collections import deque

def read_maze(filename:str)->list[str]:
    matrix:list[str]=[]
    with open(filename,"r",encoding="utf-8") as file:
        for line in file:
            matrix.append(line.rstrip("\n"))
    return matrix

def width_maze(maze:list[str])->int:
    return len(maze[0])

def is_wall(maze:list[str],wall:tuple[int,int])->bool:
    return (maze[wall[0]][wall[1]]=='#')

def find_start_and_target(maze:list[str])->tuple[tuple[int,int],tuple[int,int]]:
    for i in range(0,len(maze)):
        for j in range(0,len(maze[i])):
            if(maze[i][j]=='S'):
                xs=i
                ys=j
            elif(maze[i][j]=='T'):
                xt=i
                yt=j
    return (xs,ys),(xt,yt)

def get_neighbors(maze:list[str],position:tuple[int,int])->list[tuple[int,int]]:
    neighbors:list[tuple[int,int]]=[]
    if position[0]>0:
        if not(is_wall(maze,(position[0]-1,position[1]))):
            neighbors.append((position[0]-1,position[1]))
    if position[0]<len(maze)-1:
        if not(is_wall(maze,(position[0]+1,position[1]))):
            neighbors.append((position[0]+1,position[1]))
    if position[1]<width_maze(maze)-1:
        if not(is_wall(maze,(position[0],position[1]+1))):
            neighbors.append((position[0],position[1]+1))
    if position[1]>0:
        if not(is_wall(maze,(position[0],position[1]-1))):
            neighbors.append((position[0],position[1]-1))
    return neighbors
        
def bfs(maze:list[str],start:tuple[int,int],target:tuple[int,int])->list[tuple[int,int]]:
    q=deque([start])
    visited:set[tuple[int,int]]={start}
    parent:dict[tuple[int,int],tuple[int,int]]={start:None}
    while q:
        r,c=q.popleft()
        if(r,c)==target:
            path:list[tuple[int,int]]=[]
            current:tuple[int,int]=(r,c)
            while current is not None:
                path.append(current)
                current=parent[current]
            path.reverse()
            return path
        for nr,nc in get_neighbors(maze,(r,c)):
            if(nr,nc) not in visited:
                visited.add((nr,nc))
                parent[(nr,nc)]=(r, c)
                q.append((nr,nc))
    return []

def dfs(maze:list[str],start:tuple[int,int],target:tuple[int,int])->list[tuple[int,int]]:
    stack:list[tuple[int,int]]=[start]
    visited:set[tuple[int,int]]={start}
    parent:dict[tuple[int,int],tuple[int,int]]={start:None}

    while stack:
        coord=stack.pop()
        if coord==target:
            path:list[tuple[int,int]]=[]
            current:tuple[int,int]=coord
            while current is not None:
                path.append(current)
                current=parent[current]
            path.reverse()
            return path
        for nr,nc in reversed(get_neighbors(maze,(coord[0],coord[1]))):
            if(nr,nc) not in visited:
                visited.add((nr,nc))
                parent[(nr,nc)]=(coord[0],coord[1])
                stack.append((nr,nc))
    return []

def print_maze_with_path(maze:list[str],path:list[tuple[int,int]])->None:
    red="\033[31m"
    yellow="\033[33m"
    green= "\033[32m"
    normal="\033[0m"
    for i in range(0,len(maze)):
        row=[]
        for j in range(0,len(maze[i])):
            if(maze[i][j]=='#' or maze[i][j]=='.'):
                if(path.__contains__((i,j))):
                    row.append(f"{red}*")
                else:
                    row.append(f"{normal}{maze[i][j]}")
            elif(maze[i][j]=='S'):
                row.append(f"{yellow}S")
            elif(maze[i][j]=='T'):
                row.append(f"{green}T")
        print("".join(row))

if __name__=="__main__":
    maze=read_maze(sys.argv[2])
    start,target=find_start_and_target(maze)
    if sys.argv[1]=="bfs":
        print_maze_with_path(maze,bfs(maze,start,target))
    elif sys.argv[1]=="dfs":
        print_maze_with_path(maze,dfs(maze,start,target))
    else:
        print("not supported algorithm")