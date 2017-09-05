import pygame
from pygame.locals import *
import time
import random
pygame.init()
pygame.mixer.init()

width = 1200
height =600
gameDisplay= pygame.display.set_mode((width,height))
pygame.display.set_caption('Snakebite')

logo=pygame.image.load('snake.gif')
pygame.display.set_icon(logo)
img=pygame.image.load('snakebite.png')
img1=pygame.image.load('ratatta.png')
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
blue2=(0,162,232)
lblue2=(153,217,234)
violet=(163,73,164)
violet2=(185,122,87)
grey = (32,56,85)
green=(0,128,0)
oint=(65,155,12)
sky=(150,200,200)
ghost=(200,2,200)
faint=(200,200,200)
dark=(20,2,20)
hhh=(2,80,80)
yellow=(255,255,0)
clock= pygame.time.Clock()
block =20
FPS=20
direction = "right"
grey2=(195,195,195)


                        
#pygame.font.Font("C:/Windows/Fonts/Small Fonts Regular",60)
smallfont=pygame.font.SysFont("comicsansms",30)
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("comicsansms",100)
small1font=pygame.font.SysFont("comicsansms",18)

thick=40
def tar():
     tar_x= round(random.randrange(0,width-thick))#/10.0)*10
     tar_y= round(random.randrange(0,height-thick))#/10.0)*10
     gameDisplay.blit(img1,(tar_x,tar_y))
     return tar_x,tar_y

def snake(block, snakeList):

          
     if direction=="right":
          head=pygame.transform.rotate(img,270)

     if direction=="left":
          head=pygame.transform.rotate(img,90)

     if direction=="up":
          head=pygame.transform.rotate(img,0)

     if direction=="down":
          head=pygame.transform.rotate(img,180)
     pygame.display.update()
     gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
     for xny in snakeList[:-1]:
          pygame.draw.rect(gameDisplay,grey2,[xny[0],xny[1],block,block])


def control():
     control=pygame.mixer.music.load("control.mid")

     pygame.mixer.music.play(-1,0.0)

     control = True
     while control:
           
           for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                   pygame.quit()
                   quit()
                
           gameDisplay.fill(green)

           mes("Controls",blue2,-250,size="large")
           mes("Snake Movement",yellow,-150,size="med")
           mes("Up : Upper Arrow",faint,-90,size="small")
           mes("Down : Down Arrow",faint,-60,size="small")
           mes("Left : Left Arrow",faint,-30,size="small")
           mes("Right : Right Arrow",faint,0,size="small")
           mes("Other Controls",yellow,50,size="med")
           mes("Pause : p",faint,93,size="small")
           mes("Continue : c",faint,128,size="small")
           mes("Play : s",faint,165,size="small")
           mes("Quit : q",faint,200,size="small")

                          
           button_fun("play",black,300,530,100,50,size="small1",action = "play")
           button_fun("Main",black,550,530,100,50,size="small1",action = "Main")
           button_fun("quit",black,800,530,100,50,size="small1",action ="quit")

           pygame.display.update()
           clock.tick(15)


        
def button_fun(name,color,x,y,wid,hei,size,action=None):
     
     
     curs = pygame.mouse.get_pos()
     
     click = pygame.mouse.get_pressed()
     
     if  x + wid > curs[0] > x  and  y + hei > curs[1] > y:
            pygame.draw.rect(gameDisplay,sky,(x,y,wid ,hei))
            if click[0]==1 and action != None:
                 snake=pygame.mixer.music.load("snake_.WAV")

                 pygame.mixer.music.play(1,0.0)
                 if action == "quit":
                      pygame.quit()
                      quit()
                 elif action == "control":
                      control()
                 elif action == "play":
                      gameLoop()
                 elif action == "Main":
                      intro()
         
     else :
          pygame.draw.rect(gameDisplay,white,(x,y,wid,hei))
          
         
     mtb(name,color,x,y,wid,hei,size)
     
def intro():
     bac_s=pygame.mixer.music.load("iron man.mp3")

     pygame.mixer.music.play(-1,0.0)

     intro = True
     while intro:
           
           for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                   pygame.quit()
                   quit()
                if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_s:
                              intro =False
                        if event.key==pygame.K_q:
                              pygame.quit()
                              quit()
           
           gameDisplay.fill(green)

           mes("Welcome To Snakebite",blue,-150,size="large")
           mes("the objective of the game is to eat mouse",sky,-20,size="med")
           mes("the more mouse you eat,the longer you get",sky,40,size="med")
           mes("don't bite yourself or touch edges",sky,100,size="med")
           mes("press s to play, p to pause, or q to quit",yellow,180,size="small")

                          
           button_fun("play",black,300,530,100,50,size="small1",action = "play")
           button_fun("controls",black,550,530,100,50,size="small1",action = "control")
           button_fun("quit",black,800,530,100,50,size="small1",action ="quit")

           pygame.display.update()
           clock.tick(15)
def text_obj(text,color,size):
     if size=="small":
          texts=smallfont.render(text,True,color)
     elif size=="med":
          texts=medfont.render(text,True,color)

     elif size=="large":
          texts=largefont.render(text,True,color)
     elif size=="small1":
          texts=small1font.render(text,True,color)      
     
     return texts,texts.get_rect()

def mtb(msg,color,pos_x,pos_y,wid,hei,size):

     text_surf,textrect=text_obj(msg,color,size)
     textrect.center=((pos_x+(wid/2)),pos_y+(hei/2))
     gameDisplay.blit( text_surf,textrect)

def mes(msg,color,y_displace=0,size="small") :

     text_surf,text_rect=text_obj(msg,color,size)
     text_rect.center=(width/2),(height/2)+y_displace
     gameDisplay.blit( text_surf,text_rect)
    
def score(score):
     sc_tx= smallfont.render("Score =  " + str(score),True,white)
     gameDisplay.blit(sc_tx,[0,0])
#xo=score(score)

             
        

        
        


'''def highscore(snakeLL):
     Score = str(snakeLL)
     return Score'''
def pause():
     #gamel=pygame.mixer.music.load("gamel.WAV")

     #pygame.mixer.music.play(1,0.0)
     paused= True

     mes("Pause",sky,-100,size="large")
     mes("press c to continue or q to quit",yellow,25)
     pygame.display.update()
     while paused:
          for event in pygame.event.get():
                if event.type==pygame.QUIT:
                     pygame.quit()
                     quit()
                if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_c:
                         paused = False
                     if event.key==pygame.K_q:
                         pygame.quit()
                         quit()
                
          #gameDisplay.fill(green)
          
         
          pygame.display.update()
     clock.tick(10)
def gameLoop():
    gameloop=pygame.mixer.music.load("gameloop.mid")

    pygame.mixer.music.play(-1,0.0)

    global direction
    gameExit=False
    gameOver=False
    
    snakeList=[]
    snakeL=1
    thick=40
    
    lead_x=width/2
    lead_y=height/2
    lead=0
    lead1=0
    tar_x,tar_y = tar()
    while not gameExit:
        
        while gameOver==True:
            #Score = highscore(score)
            gameDisplay.fill(black)
            mes("Game Over ",oint,-50,size="large")
            mes("press s to play again or q to quit ",sky,50,size="med")
            mes("Your Score : "+ str(Score),sky,150,size="med")
            
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                     gameOver=False
                     gameExit=True
                if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_s:
                         gameLoop()
                     if event.key==pygame.K_q:
                         gameExit=True
                         gameOver=False
                
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction="left"
                    lead=-block
                    lead1=0

                elif event.key==pygame.K_RIGHT:
                    direction="right"
                    lead=block
                    lead1=0
                    
                
                elif event.key==pygame.K_UP:
                    direction="up"
                    lead1=-block
                    lead=0
                elif event.key==pygame.K_DOWN:
                    direction="down"
                    lead1=block
                    lead=0
                elif event.key==pygame.K_p:
                    pause()
        if lead_x >= width or lead_x <=0 or lead_y >= 600 or lead_y <=0   :
             butt=pygame.mixer.music.load("button.mp3") 
             pygame.mixer.music.play(1,0.0)
             
             gameOver=True

        lead_x+=lead
        lead_y+=lead1

        gameDisplay.fill(black)
        gameDisplay.blit(img1,(tar_x,tar_y))
        
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeL:
             del snakeList[0]
        for eachSeg in snakeList[:-1]:
             if eachSeg == snakeHead:
                  
                  gameOver=True
                  
        snake(block, snakeList)

        score(snakeL-1)
        Score= snakeL-1
        #scr = Score
        
        
        
            
        '''Highscore = snakeL-1
        for so in Highscore :
             if (so < score):
                  Highscore = Score'''
        pygame.display.update()
        
 #       if lead_x==tar_x and lead_y==tar_y:
             
        if lead_x > tar_x and lead_x < tar_x + thick or lead_x + block > tar_x and lead_x  + block < tar_x + thick:
            if lead_y > tar_y and lead_y < tar_y + thick:
                 tar_x,tar_y = tar()
                 
                 snakeL+=1
                  
            elif lead_y + block > tar_y and lead_y + block < tar_y + thick:
                 tar_x,tar_y = tar()
                 
                 snakeL+=1
                 
        clock.tick(FPS)      
    pygame.quit()
    quit()
intro()
gameLoop()

