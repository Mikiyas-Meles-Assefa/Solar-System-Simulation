import pygame
import math


pygame.init()
window_width, window_height = 1380, 780
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Planetary Motion")


FONT=pygame.font.SysFont("comicsans",20)
FONT1=pygame.font.SysFont("comicsans",34)
points = []
with open("earth.dat", "r") as file:
    for line in file:
        x, y = map(float, line.strip().split())
        points.append((x, y))
        
points2=[]
with open("mercury.dat","r") as file:
    for line in file:
        x,y=map(float,line.strip().split())
        points2.append((x,y))
points3=[]
with open("sun.dat","r") as file:
    for line in file:
        x,y=map(float,line.strip().split())
        points3.append((x,y))
points4=[]
with open("venus.dat","r") as file:
    for line in file:
        x,y=map(float,line.strip().split())
        points4.append((x,y))
points5=[]
with open("mars.dat","r") as file:
    for line in file:
        x,y=map(float,line.strip().split())
        points5.append((x,y))
points6=[]
with open("jupiter.dat","r") as file:
    for line in file:
        x,y=map(float,line.strip().split())
        points6.append((x,y))
points7=[]
with open("saturn.dat","r") as file:
    for line in file:
        x,y=map(float,line.strip().split())
        points7.append((x,y))
points8=[]
with open("uranus.dat","r") as file:
    for line in file:
        x,y=map(float,line.strip().split())
        points8.append((x,y))
points9=[]
with open("Neptune.dat","r") as file:
    for line in file:
        x,y=map(float,line.strip().split())
        points9.append((x,y))





FPS = (60)
clock = pygame.time.Clock()


color1= [79,76,176]
color2=[253,184,19]
color3=[255,0,0]
color4=[0,251,2]
color5=[173,98,66]
color6=[225,225,226]
color7=[250,229,191]
color8=[172,229,238]
color9=[0,125,172]

AA=updated_list= []
BB=updated_list2=[]
CC=updated_list3=[]
DD=updated_list4=[]
EE=updated_list5=[]
FF=updated_list6=[]
GG=updated_list7=[]
HH=updated_list8=[]
II=updated_list9=[]


   
def draw_mercury(x,y,i,CC):
    mercury_radius=1.9
    merc_color=color3
    merc_position=(int(x) + window_width // 2, int(y) + window_height // 2)
    a,b=merc_position
    updated_list3=CC
    updated_list3.append((a,b))
    if i<10:
        distance_to_sun =math.sqrt(x**2+y**2)
        distance_text=FONT.render(f"{round(distance_to_sun*10e-1,1)} million kms",1,[255,255,255])

        if len(updated_list3)>10:
            if len(updated_list3)<91:
                pygame.draw.lines(window,merc_color,False,updated_list3)
            else:
                updated_list3=updated_list3[len(updated_list3)-91:len(updated_list3)-1]
                pygame.draw.lines(window,merc_color,False,updated_list3)
    #pygame.draw.circle(window,merc_color,merc_position,mercury_radius)
    image=pygame.image.load("mercury.png")
    image=pygame.transform.scale(image, (14,16))
    window.blit(image,(a-image.get_width()/2,b-image.get_height()/2+mercury_radius))
    #window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2+mercury_radius))
    

def draw_earth(x, y,hour,i,AA):
    earth_radius = 2
    earth_color = color4 
    earth_position = (int(x) + window_width // 2, int(y) + window_height // 2) 
    a,b=earth_position
    updated_list4=AA
    updated_list4.append((a,b))
    if i<10:
        
        if len(updated_list4)>10:
            if len(updated_list4)<101:
                pygame.draw.lines(window,earth_color,False,updated_list4)
            else:
                updated_list4=updated_list4[len(updated_list4)-101:len(updated_list4)-1]
                pygame.draw.lines(window,earth_color,False,updated_list4)
    pygame.draw.circle(window, earth_color, earth_position, earth_radius)
    image=pygame.image.load("earth.png")
    image=pygame.transform.scale(image, (23,27))
    window.blit(image,(a-image.get_width()/2,b-image.get_height()/2+earth_radius))
    #window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2+earth_radius))
    distance_to_sun =math.sqrt(x**2+y**2)
    distance_text=FONT.render(f"{round(distance_to_sun*10e-1,1)} million kms",1,[255,255,255])
    #window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2))


def draw_sun(x, y,BB):
    earth_radius = 35

    earth_color = color2  
    earth_position = (int(x) + window_width // 2, int(y) + window_height // 2)  
    a,b=earth_position
    updated_list2=BB
    updated_list2.append((a,b))

    if len(updated_list2)>10:
        if len(updated_list2)<10001:
            pygame.draw.lines(window,earth_color,False,updated_list2)
        else:
            updated_list2.pop(0)
            pygame.draw.lines(window,earth_color,False,updated_list2)
    image=pygame.image.load("sun.png")
    image=pygame.transform.scale(image, (100,100))
    
    window.blit(image,(a-image.get_width()/2,b-image.get_height()/2))
    #pygame.draw.circle(window, earth_color, earth_position, earth_radius)

def draw_venus(x, y,i,DD):
    earth_radius = 2
    earth_color = color4 
    earth_position = (int(x) + window_width // 2, int(y) + window_height // 2) 
    a,b=earth_position
    updated_list4=DD
    updated_list4.append((a,b))
    if i<10:
        
        if len(updated_list4)>10:
            if len(updated_list4)<101:
                pygame.draw.lines(window,earth_color,False,updated_list4)
            else:
                updated_list4=updated_list4[len(updated_list4)-101:len(updated_list4)-1]
                pygame.draw.lines(window,earth_color,False,updated_list4)
    pygame.draw.circle(window, earth_color, earth_position, earth_radius)
    image=pygame.image.load("venus.png")
    image=pygame.transform.scale(image, (15,17))
    window.blit(image,(a-image.get_width()/2,b-image.get_height()/2+earth_radius))
    #window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2+earth_radius))
    distance_to_sun =math.sqrt(x**2+y**2)
    distance_text=FONT.render(f"{round(distance_to_sun*10e-1,1)} million kms",1,[255,255,255])
    #window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2))

def draw_mars(x,y,i,EE):
    mercury_radius=11
    merc_color=color5
    merc_position=(int(x) + window_width // 2, int(y) + window_height // 2)
    a,b=merc_position
    updated_list5=EE
    updated_list5.append((a,b))
    if i < 10:
        
        if len(updated_list5)>10:
            if len(updated_list5)<181:
                pygame.draw.lines(window,merc_color,False,updated_list5)
            else:
                updated_list5=updated_list5[len(updated_list5)-181:len(updated_list5)-1]
                pygame.draw.lines(window,merc_color,False,updated_list5)
    #pygame.draw.circle(window,merc_color,merc_position,mercury_radius)
    image=pygame.image.load("mars.png")
    image=pygame.transform.scale(image, (24,25))
    window.blit(image,(a-image.get_width()/2,b-image.get_height()/2+mercury_radius))
    distance_to_sun =math.sqrt(x**2+y**2)
    distance_text=FONT.render(f"{round(distance_to_sun*10e-1,1)} million kms",1,[255,255,255])
    distance_to_sun =math.sqrt(x**2+y**2)
    distance_text=FONT.render(f"{round(distance_to_sun*10e-1,1)} million kms",1,[255,255,255])
    #window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2+mercury_radius))

    #window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2+mercury_radius))
def draw_jupiter(x,y,i,FF):
    mercury_radius=17
    merc_color=color6
    merc_position=(int(x) + window_width // 2, int(y) + window_height // 2)
    a,b=merc_position
    updated_list6=FF
    updated_list6.append((a,b))
    if i<10:
        
        if len(updated_list6)>10:
            if len(updated_list6)<3001:
                pygame.draw.lines(window,merc_color,False,updated_list6)
            else:
                updated_list6=updated_list6[len(updated_list6)-3001:len(updated_list6)-1]
                pygame.draw.lines(window,merc_color,False,updated_list6)
    #pygame.draw.circle(window,merc_color,merc_position,mercury_radius)
    image=pygame.image.load("jupiter.png")
    image=pygame.transform.scale(image, (68,65))
    window.blit(image,(a-image.get_width()/2,b-image.get_height()/2+mercury_radius))
    distance_to_sun =math.sqrt(x**2+y**2)
    distance_text=FONT.render(f"{round(distance_to_sun/0.033,1)} million kms",1,[255,255,255])
    distance_to_sun =math.sqrt(x**2+y**2)
    distance_text=FONT.render(f"{round(distance_to_sun*10e-1,1)} million kms",1,[255,255,255])
   # window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2+mercury_radius))

    #window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2+mercury_radius))
def draw_saturn(x,y,i,GG):
    mercury_radius=14.5
    merc_color=color7
    merc_position=(int(x) + window_width // 2, int(y) + window_height // 2)
    a,b=merc_position
    updated_list7=GG
    updated_list7.append((a,b))
    if i<10:
        
        if len(updated_list7)>10:
            if len(updated_list7)<7001:
                pygame.draw.lines(window,merc_color,False,updated_list7)
            else:
                updated_list7=updated_list7[len(updated_list7)-7001:len(updated_list7)-1]
                pygame.draw.lines(window,merc_color,False,updated_list7)
    image=pygame.image.load("saturn.png")
    image=pygame.transform.scale(image, (84,70))
    window.blit(image,(a-image.get_width()/2,b-image.get_height()/2+mercury_radius))
    distance_to_sun =math.sqrt(x**2+y**2)
    distance_text=FONT.render(f"{round(distance_to_sun*10e-1,1)} million kms",1,[255,255,255])
   # window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2+mercury_radius))

    #window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2+mercury_radius))
def draw_uranus(x,y,i,HH):
    mercury_radius=12.5
    merc_color=color8
    merc_position=(int(x) + window_width // 2, int(y) + window_height // 2)
    a,b=merc_position
    updated_list8=HH
    updated_list8.append((a,b))
    if i<10:
       
        if len(updated_list8)>10:
            if len(updated_list8)<8001:
                pygame.draw.lines(window,merc_color,False,updated_list8)
            else:
                updated_list8=updated_list8[len(updated_list8)-8001:len(updated_list8)-1]
                pygame.draw.lines(window,merc_color,False,updated_list8)
    #pygame.draw.circle(window,merc_color,merc_position,mercury_radius)
    image=pygame.image.load("uranus.png")
    image=pygame.transform.scale(image, (64,56))
    window.blit(image,(a-image.get_width()/2,b-image.get_height()/2+mercury_radius))
    distance_to_sun =math.sqrt(x**2+y**2)
    distance_text=FONT.render(f"{round(distance_to_sun*10e-1,1)} million kms",1,[255,255,255])
   # window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2+mercury_radius))

    #window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2+mercury_radius))
def draw_neptune(x,y,i,II):
    mercury_radius=10
    merc_color=color9
    merc_position=(int(x) + window_width // 2, int(y) + window_height // 2)
    a,b=merc_position
    updated_list9=II
    updated_list9.append((a,b))
    if i<10:
        
        if i<10:
            if len(updated_list9)>10  :
                if len(updated_list9)<12001:
                    pygame.draw.lines(window,merc_color,False,updated_list9)
                else:
                    updated_list9=updated_list9[len(updated_list9)-12001:len(updated_list9)-1]
                    pygame.draw.lines(window,merc_color,False,updated_list9)
        #pygame.draw.circle(window,merc_color,merc_position,mercury_radius)
    image=pygame.image.load("neptune.png")
    image=pygame.transform.scale(image, (25,25))
    window.blit(image,(a-image.get_width()/2,b-image.get_height()/2+mercury_radius))
    
    distance_to_sun =math.sqrt(x**2+y**2)
    distance_text=FONT.render(f"{round(distance_to_sun*10e-1,1)} million kms",1,[255,255,255])
   # window.blit(distance_text,(a-distance_text.get_width()/2,b-distance_text.get_height()/2+mercury_radius))


def draw_orbit(array,array2,array3):
    
    for i in array:
            for j in array2:
                for k in array3:
                    if len(j[0:k])>2 and (array2.index(j)+1)==i and i==array3.index(k)+1:       
                        pygame.draw.lines(window,globals()["color"+str(i)],False,j[0:k])
                        print(i)
                    
    
#print(len(points4))






def animate():
    global points
    
    input_box = pygame.Rect(window_width-400, 100, 140, 40)
    color = pygame.Color('lightskyblue3')
    active = False
    text="1"
    done = False

    running = True
    i=1
    index = 0
    index2 =0
    index3=0
    index4=0
    index5 = 0
    index6 =0
    index7=0
    index8=0
    index9=0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active= not active
                else:
                    active=False
                if active ==True:
                    color = pygame.Color('dodgerblue2')
                else:
                    color = pygame.Color('lightskyblue3')
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        i=int(text)
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode                    


        window.fill((0, 0, 0))  
        image4=pygame.image.load("back.jfif")
        image4=pygame.transform.scale(image4, (window_width,window_height))
        window.blit(image4,(0,0))
    
        
        #draw_orbit()
        hours=(index*24)%24
        
        array=[1,2,3,4,5,6,7,8,9]
        
        x2,y2=points2[index2]
        draw_mercury(x2,y2,i,CC)
        x, y = points[index]
        draw_earth(x, y,hours,i,AA)
        x3,y3=points3[index3]
        draw_sun(x3,y3,BB)
        x4,y4=points4[index4]
        draw_venus(x4,y4,i,DD)
        x5, y5 = points5[index5]
        draw_mars(x5, y5,i,EE)
        x6,y6=points6[index6]
        draw_jupiter(x6,y6,i,FF)
        x7,y7=points7[index7]
        draw_saturn(x7,y7,i,GG)
        x8,y8=points8[index8]
        draw_uranus(x8,y8,i,HH)
        x9,y9=points9[index9]
        draw_neptune (x9,y9,i,II)
        time=FONT1.render(f"{round(index/365.25,1)} Earth years",1,[255,255,255])
        window.blit(time,(window_width-500,10))
        #array2=[points,points2,points3,points4,points5,points6,points7,points8,points9]
        #array3=[index,index2,index3,index4,index5,index6,index7,index8,index9]
        #draw_orbit(array,array2,array3)



       

        text4=FONT1.render(f"Speed",1,[255,255,255])
        window.blit(text4,(window_width-500,100))
        txt_surface = FONT1.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        window.blit(txt_surface, (input_box.x + 5, input_box.y-3 ))
        pygame.draw.rect(window, color, input_box, 2)



        pygame.display.flip() 
        clock.tick(FPS)  
        
        

        index= (index + i ) % len(points)  
        index2 = (index2+ i)% len(points2)
        index3 = (index3 + i) % len(points3)  
        index4 = (index4+ i)% len(points4)
        index5= (index5 + i ) % len(points5)  
        index6 = (index6+ i)% len(points6)
        index7 = (index7 +i) % len(points7)  
        index8 = (index8+ i)% len(points8) 
        index9 = (index9+ i)% len(points9)

    pygame.quit()



animate()
