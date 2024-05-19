# 백준 2667번 단지 번호붙이기                                                                                                                                                             
N = int(input())  # N: 지도의 크기                                                                                                                                                   
maps = [input() for _ in range(N)]  # 지도                                                                                                                                        
visit = [[False] * N for _ in range(N)]                                                                                                                                         
# 지도를 확인하여 단지의 수와 각 단지 내의 집의 수를 오름차순으로 출력하라                                                                                                                                     
# 단지는 서로 연결되어있는 집들의 집합이며, 연결되어있다는 것은 집을 기준으로 상, 하, 좌, 우 한칸 옆에 있는 경우를 말한다.                                                                                                       
# DFS 함수가 실행되었다는 것은 하나의 단지를 찾았다는 의미                                                                                                                                             
                                                                                                                                                                                
danji = 0                                                                                                                                                                       
counts = [0]                                                                                                                                                                    
                                                                                                                                                                                
def DFS(x,y):                                                                                                                                                                   
    visit[x][y] = True                                                                                                                                                          
    counts[-1] += 1                                                                                                                                                             
    for nx,ny in [[x-1,y], [x+1,y], [x,y-1], [x,y+1]]:                                                                                                                          
        if 0 <= nx < N and 0 <= ny < N:                                                                                                                                         
            if visit[nx][ny] == False and maps[nx][ny] == '1':                                                                                                                  
                DFS(nx,ny)                                                                                                                                                      
                                                                                                                                                                                
for i in range(N):                                                                                                                                                              
    for j in range(N):                                                                                                                                                          
        if maps[i][j] == '1' and visit[i][j] == False:                                                                                                                          
            DFS(i,j)                                                                                                                                                            
            danji += 1                                                                                                                                                          
            counts.append(0)                                                                                                                                                    
                                                                                                                                                                                
counts.sort()                                                                                                                                                                   
print(danji)                                                                                                                                                                    
counts.pop(0)                                                                                                                                                                   
for c in counts:                                                                                                                                                                
    print(c)                                                                                                                                                                    
                                                                                                                                                                                
                                                                                                                                                                                
"""                                                                                                                                                                             
7                                                                                                                                                                               
0110100                                                                                                                                                                         
0110101                                                                                                                                                                         
1110101                                                                                                                                                                         
0000111                                                                                                                                                                         
0100000                                                                                                                                                                         
0111110                                                                                                                                                                         
0111000                                                                                                                                                                         
"""                                                                                                                                                                             
