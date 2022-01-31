import sys, pygame
import random
import numpy as np

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (250 ,0 ,0 )
WINDOW_HEIGHT = 512
WINDOW_WIDTH = 512


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)
    arr = generator()
    
    for row in arr:
        print(row)
    print(np.sum(arr))

    while True:
        drawGrid(arr)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def generator():
    print("hello world")
    
    rows, cols = (128, 128)
    percentage = 70
    arr=[]
    
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(0)
        arr.append(col)


    while(np.sum(arr)<(rows*cols*(percentage/100))):
        x = random.randrange(0,rows,1)
        y = random.randrange(0,cols,1)
        # print(x+1,y+1)
        print(np.sum(arr))
        shape = random.randrange(1,5,1)
        # print(shape)
        if(shape ==1):
            arr[x][y] = 1
            if(x+1<rows):
                arr[x+1][y] = 1
            if(x+2<rows):
                arr[x+2][y] = 1
            if(x+3<rows):
                arr[x+3][y] = 1
        elif(shape ==2):
            arr[x][y] = 1
            if(y+1<cols):
                arr[x][y+1] = 1
            if(x+1<rows and y+1<cols):
                arr[x+1][y+1] = 1
            if(x+2<rows and y+1<cols):
                arr[x+2][y+1] = 1
        elif(shape ==3):
            arr[x][y] = 1
            if(x+1<rows):
                arr[x+1][y] = 1
            if(x+1<rows and y+1<cols):
                arr[x+1][y+1] = 1
            if(x+2<rows and y+1<cols):
                arr[x+2][y+1] = 1
        else:
            arr[x][y] = 1
            if(x+1<rows and y-1>=0):
                arr[x+1][y-1] = 1
            if(x+1<rows):
                arr[x+1][y] = 1
            if(x+2<rows):
                arr[x+2][y] = 1

    # for row in arr:
    #     print(row)
    # print(np.sum(arr))
    return arr

def drawGrid(arr):
    blockSize = 4 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            if(arr[int(y/blockSize)][int(x/blockSize)]==1):     
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, RED, rect, 0)
            else:
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)

if __name__ == "__main__":
    main()