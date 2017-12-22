import pygame
import random

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('My first Pygame')
img=pygame.image.load('head.png')
pygame.display.set_icon(img)
dirn="right"

clock = pygame.time.Clock()
font= pygame.font.SysFont("comicsansms", 35)

def score(score):
	t=font.render("Score: "+str(score), True, (0,0,0))
	gameDisplay.blit(t,[0,0])
# Snake class
class Snake:

    # Initializes a Snake object
    def __init__(self, x, y, startLength):
        self.startLength = startLength
        self.startX = x
        self.startY = y
        self.reset()

    # Resets snake back to its original state
    def reset(self):
        self.pieces = []
        self.direction = 1

        for n in range(0, self.startLength):
            self.pieces.append((self.startX, self.startY + n))

    # Changes the direction of the snake
    def changeDirection(self, direction):
        # Moving in the opposite direction of current movement is not allowed
        if self.direction == 1 and direction == 2: return
        if self.direction == 2 and direction == 1: return
        if self.direction == 3 and direction == 4: return
        if self.direction == 4 and direction == 3: return

        self.direction = direction

    # Returns the head piece of the snake
    def getHead(self):
        return self.pieces[0]

    # Returns the tail piece of the snake	

def pause():
        paused=True
        while paused:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_c:
                                paused=False
                        if event.key==pygame.K_q:
                                pygame.quit()
                                quit()
                message("Paused",(0,0,0))
                message("C to continue, Q to Quit",(200,0,0),40)
                pygame.display.update()
                clock.tick(5)

def intro():
    i=True
    while i:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    i=False
        gameDisplay.fill((255,255,255))
        message("Welcome to Snakes!!",(200,0,100),-30)
        message("Press C to continue",(100,0,100),80)
        pygame.display.update()
        clock.tick(15)

def message(m,color,dispy=0):
    text= font.render(m, True, color)
    t=text.get_rect()
    t.center=(400),(300)+dispy
    gameDisplay.blit(text, t)
    
class Player:
    x = 10
    y = 10
    speed = 1
 
    def moveRight(self):
        self.x = self.x + self.speed
 
    def moveLeft(self):
        self.x = self.x - self.speed
 
    def moveUp(self):
        self.y = self.y - self.speed
 
    def moveDown(self):
        self.y = self.y + self.speed
    gameDisplay.blit(head, [snakeList[-1][0],snakeList[-1][1]])

def gameLoop():
    global dirn
    pyExit=False
    pyOver=False
    x=400
    y=300
    x_change=0
    y_change=0
    snakeList=[]
    snakeLen=1
    foodX=round(random.randrange(0,790)/10.0)*10.0
    foodY=round(random.randrange(0,590)/10.0)*10.0
    while not pyExit:
        while pyOver:
            gameDisplay.fill((255,255,255))
            message("Game Over! Press C to play Again, Q to Quit",(255,0,0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pyExit=True
                        pyOver=False
                    if event.key==pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pyExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    dirn="left"
                    x_change=-10
                    y_change=0
                if event.key==pygame.K_RIGHT:
                    dirn="right"
                    x_change=10
                    y_change=0
                if event.key==pygame.K_UP:
                    dirn="up"
                    y_change=-10
                    x_change=0
                if event.key==pygame.K_DOWN:
                    dirn="down"
                    y_change=10
                    x_change=0
                if event.key==pygame.K_p:
                    pause()

        if x>=800:
            x=10
        if y>=600:
            y=10
        if x<=0:
            x=800
        if y<=0:
            y=600

        x+=x_change
        y+=y_change
        gameDisplay.fill((255,255,255))
        pygame.draw.rect(gameDisplay, (0,255,0), [foodX,foodY,10,10])
        
        snakeHead=[]
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLen:
            del snakeList[0]
        for body in snakeList[:-1]:
            if body==snakeHead:
                pyOver=True

        snake(snakeList)
        score(snakeLen-1)
        pygame.display.update()
        clock.tick(25)

        if foodX==x and foodY==y:
                foodX=round(random.randrange(0,790)/10.0)*10.0
                foodY=round(random.randrange(0,590)/10.0)*10.0
                snakeLen+=1

    pygame.quit()
    quit()

intro()
gameLoop()
