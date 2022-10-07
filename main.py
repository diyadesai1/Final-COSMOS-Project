import pygame 
import os
import random
from settings import *

#SETTING SCREEN
screenLength = 500
screenHeight = 650
dim_field = (screenLength,screenHeight)
screen = pygame.display.set_mode(dim_field)

#MAZE

mazecolor = red

mazerect1 = pygame.Rect(0+25,0+45,2,160)
mazerect1b = pygame.Rect(10+25,10+45,2,140)

#first 
mazerect2 = pygame.Rect(10+25,150+45,80,2)
mazerect2b = pygame.Rect(0+25,160+45,80,2)

mazerect3 = pygame.Rect(90+25,150+45,2,50)
mazerect3b = pygame.Rect(80+25,160+45,2,30)

mazerect4 = pygame.Rect(0+25,190+45,80,2)
mazerect4b = pygame.Rect(0+25,200+45,90,2)

#second entry
mazerect5 = pygame.Rect(0+25,240+45,90,2)
mazerect5b = pygame.Rect(0+25,250+45,80,2)

mazerect6 = pygame.Rect(90+25,240+45,2,50)
mazerect6b = pygame.Rect(80+25,250+45,2,30)

mazerect7 = pygame.Rect(0+25,280+45,80,2)
mazerect7b = pygame.Rect(10+25,290+45,80,2)

mazerect8 = pygame.Rect(0+25,280+45,2,170)
mazerect8b = pygame.Rect(10+25,290+45,2,80)

# mazerect9 = pygame.Rect(10+25,360+45,40,2)
# mazerect9b = pygame.Rect(10+25,370+45,40,2)

# mazerect10 = pygame.Rect(50+25,360+45,2,10)
mazerect10b = pygame.Rect(10+25,370+45,2,70)

#bottom

mazerect11 = pygame.Rect(0+25,448+45,450,2)
mazerect11b = pygame.Rect(10+25,440+45,430,2)


# #right wall second entry

mazerect12 = pygame.Rect(360+25,240+45,90,2)
mazerect12b = pygame.Rect(370+25,250+45,80,2)

mazerect13 = pygame.Rect(360+25,240+45,2,50)
mazerect13b = pygame.Rect(370+25,250+45,2,30)

mazerect14 = pygame.Rect(370+25,280+45,80,2)
mazerect14b = pygame.Rect(360+25,290+45,80,2)

mazerect15 = pygame.Rect(449+25,280+45,2,170)
mazerect15b = pygame.Rect(440+25,290+45,2,80)

# mazerect16 = pygame.Rect(400+25,360+45,40,2)
# mazerect16b = pygame.Rect(400+25,370+45,40,2)

# mazerect17 = pygame.Rect(400+25,360+45,2,10)
mazerect17b = pygame.Rect(440+25,370+45,2,70)

#right wall first entry
mazerect18 = pygame.Rect(360+25,150+45,80,2)
mazerect18b = pygame.Rect(370+25,160+45,80,2)

mazerect19 = pygame.Rect(360+25,150+45,2,50)
mazerect19b = pygame.Rect(370+25,160+45,2,30)

mazerect20 = pygame.Rect(370+25,190+45,80,2)
mazerect20b = pygame.Rect(360+25,200+45,90,2)

mazerect21 = pygame.Rect(449+25,0+45,2,160)
mazerect21b = pygame.Rect(440+25,10+45,2,140)

#Top maze

mazerect22 = pygame.Rect(0+25,0+45,450,2)
mazerect22b = pygame.Rect(10+25,10+45,210,2)
mazerect23 = pygame.Rect(230+25,10+45,210,2)

mazerect23b = pygame.Rect(220+25,10+45,2,150)
mazerect24 = pygame.Rect(230+25,10+45,2,150)
mazerect24b = pygame.Rect(220+25,160+45,10,2)

mazeblock1 = pygame.Rect(180+25,240+45,90,2)
mazeblock2 = pygame.Rect(180+25,200+45,30,2)
mazeblock3 = pygame.Rect(180+25,200+45,2,40)

mazeblock4 = pygame.Rect(170+25,190+45,2,60)
mazeblock5 = pygame.Rect(280+25,190+45,2,60)

mazeblock6 = pygame.Rect(170+25,250+45,110,2)


mazeblock7 = pygame.Rect(240+25,200+45,30,2)
mazeblock8 = pygame.Rect(270+25,200+45,2,40)
mazeblock9 = pygame.Rect(170+25,190+45,40,2)
mazeblock10 = pygame.Rect(240+25,190+45,40,2)

#close sides
mazeblock11 = pygame.Rect(208+25,190+45,2,10)
mazeblock12 = pygame.Rect(240+25,190+45,2,10)

#squares
mazeblock13 = pygame.Rect(55+25,45+45,2,10)
mazeblock14 = pygame.Rect(165+25,45+45,2,130)

mazeblock15 = pygame.Rect(55+25,45+45,110,2)
mazeblock16 = pygame.Rect(55+25,55+45,100,2)

mazeblock16b = pygame.Rect(155+25,55+45,2,120)
mazeblock16c = pygame.Rect(155+25,175+45,10,2)


#SQUARE BELOW RECTANGLE
mazeblock17 = pygame.Rect(55+25,90+45,2,25)
mazeblock18 = pygame.Rect(105+25,90+45,2,25)
mazeblock19 = pygame.Rect(55+25,90+45,50,2)

mazeblock20 = pygame.Rect(55+25,115+45,50,2)

#RECTANGLES ON THE RIGHT!!!
mazeblock21 = pygame.Rect(395+25,45+45,2,10)
mazeblock22 = pygame.Rect(285+25,45+45,2,130)

mazeblock23 = pygame.Rect(285+25,45+45,110,2)
mazeblock24 = pygame.Rect(295+25,55+45,100,2)

mazeblock25 = pygame.Rect(295+25,55+45,2,120)
mazeblock26 = pygame.Rect(285+25,175+45,10,2)


#SQUARE
mazeblock27 = pygame.Rect(345+25,90+45,2,25)
mazeblock28 = pygame.Rect(395+25,90+45,2,25)
mazeblock29 = pygame.Rect(345+25,90+45,50,2)

mazeblock30 = pygame.Rect(345+25,115+45,50,2)


#BOTTOM MAZE
bottomBlock1 = pygame.Rect(180+25,300+45,40,2)
bottomBlock2 = pygame.Rect(180+25,290+45,90,2)
bottomBlock3 = pygame.Rect(180+25,290+45,2,10)
bottomBlock4 = pygame.Rect(270+25,290+45,2,10)
bottomBlock5 = pygame.Rect(230+25,300+45,40,2)
bottomBlock6 = pygame.Rect(220+25,300+45,2,100)
bottomBlock7 = pygame.Rect(230+25,300+45,2,100)
bottomBlock8 = pygame.Rect(220+25,400+45,10,2)
bottomBlock9 = pygame.Rect(60+25,330+45,10,2)
bottomBlock10 = pygame.Rect(60+25,330+45,2,80)
bottomBlock11 = pygame.Rect(70+25,330+45,2,70)

bottomBlock12 = pygame.Rect(60+25,410+45,100,2)
bottomBlock13 = pygame.Rect(70+25,400+45,90,2)
bottomBlock14 = pygame.Rect(160+25,400+45,2,10)
bottomBlock15 = pygame.Rect(115+25,370+45,55,2)
bottomBlock16 = pygame.Rect(115+25,330+45,55,2)
bottomBlock17 = pygame.Rect(115+25,330+45,2,40)
bottomBlock18 = pygame.Rect(170+25,330+45,2,40)

bottomBlock19 = pygame.Rect(290+25,410+45,100,2)
bottomBlock20 = pygame.Rect(290+25,400+45,90,2)
bottomBlock21 = pygame.Rect(290+25,400+45,2,10)
bottomBlock22 = pygame.Rect(280+25,370+45,55,2)
bottomBlock23 = pygame.Rect(280+25,330+45,55,2)
bottomBlock24 = pygame.Rect(335+25,330+45,2,40)
bottomBlock25 = pygame.Rect(280+25,330+45,2,40)
bottomBlock26 = pygame.Rect(380+25,330+45,10,2)
bottomBlock27 = pygame.Rect(390+25,330+45,2,80)
bottomBlock28 = pygame.Rect(380+25,330+45,2,70)

doorblock = pygame.Rect(213+25,192+45,25,2)





# LIST
walls = [mazerect1, mazerect1b,mazerect2,mazerect2b, mazerect3, mazerect3b, mazerect4, mazerect4b, mazerect5, mazerect5b, mazerect6, mazerect6b, mazerect7,mazerect7b, mazerect8, mazerect8b, mazerect10b, mazerect11, mazerect11b, mazerect12, mazerect12b, mazerect13, mazerect13b, mazerect14, mazerect14b, mazerect15, mazerect15b, mazerect17b, mazerect18, mazerect18b, mazerect19, mazerect19b, mazerect20, mazerect20b, mazerect21, mazerect21b, mazerect22, mazerect22b, mazerect23, mazerect23b, mazerect24, mazerect24b, mazeblock1, mazeblock2, mazeblock3, mazeblock4, mazeblock5, mazeblock6, mazeblock7, mazeblock8,mazeblock9, mazeblock10,mazeblock11,mazeblock12, mazeblock13,mazeblock14,mazeblock15,mazeblock16,mazeblock16b,mazeblock16c, mazeblock17,mazeblock18,mazeblock19,mazeblock20,mazeblock21,mazeblock22,mazeblock23,mazeblock24,mazeblock25,mazeblock26,mazeblock27,mazeblock28,mazeblock29,mazeblock30,bottomBlock1,bottomBlock2,bottomBlock3,bottomBlock4,bottomBlock5,bottomBlock6,bottomBlock7,bottomBlock8,bottomBlock9,bottomBlock10,bottomBlock11,bottomBlock12, bottomBlock13,bottomBlock14,bottomBlock15,bottomBlock16,bottomBlock17,bottomBlock18,bottomBlock19,bottomBlock20, bottomBlock21,bottomBlock22,bottomBlock23,bottomBlock24,bottomBlock25,bottomBlock26,bottomBlock27,bottomBlock28]

rect_list = [mazerect1, mazerect1b,mazerect2,mazerect2b, mazerect3, mazerect3b, mazerect4, mazerect4b, mazerect5, mazerect5b, mazerect6, mazerect6b, mazerect7,mazerect7b, mazerect8, mazerect8b, mazerect10b, mazerect11, mazerect11b, mazerect12, mazerect12b, mazerect13, mazerect13b, mazerect14, mazerect14b, mazerect15, mazerect15b, mazerect17b, mazerect18, mazerect18b, mazerect19, mazerect19b, mazerect20, mazerect20b, mazerect21, mazerect21b, mazerect22, mazerect22b, mazerect23, mazerect23b, mazerect24, mazerect24b, mazeblock4, mazeblock5, mazeblock6, mazeblock7, mazeblock8,mazeblock9, mazeblock10,mazeblock11,mazeblock12, mazeblock13,mazeblock14,mazeblock15,mazeblock16,mazeblock16b,mazeblock16c, mazeblock17,mazeblock18,mazeblock19,mazeblock20,mazeblock21,mazeblock22,mazeblock23,mazeblock24,mazeblock25,mazeblock26,mazeblock27,mazeblock28,mazeblock29,mazeblock30,bottomBlock1,bottomBlock2,bottomBlock3,bottomBlock4,bottomBlock5,bottomBlock6,bottomBlock7,bottomBlock8,bottomBlock9,bottomBlock10,bottomBlock11,bottomBlock12, bottomBlock13,bottomBlock14,bottomBlock15,bottomBlock16,bottomBlock17,bottomBlock18,bottomBlock19,bottomBlock20, bottomBlock21,bottomBlock22,bottomBlock23,bottomBlock24,bottomBlock25,bottomBlock26,bottomBlock27,bottomBlock28]

#mazerect9, mazerect9b, mazerect10
#mazerect16, mazerect16b, mazerect17,

#LOAD IMAGE
monopoly = pygame.image.load(os.path.join("assets", "monopoly.png"))
monopoly2 = pygame.image.load(os.path.join("assets", "monopoly2.png"))
monopolyflip = pygame.image.load(os.path.join("assets", "monopolyflip.png"))
monopolyflip2 = pygame.image.load(os.path.join("assets", "monopolyflip2.png"))
police = pygame.image.load(os.path.join("assets", "police.png"))
policewalk = pygame.image.load(os.path.join("assets", "policewalk.png"))
gamemap = pygame.image.load(os.path.join("assets", "gamemap.png"))
blackground = pygame.image.load(os.path.join("assets", "blackground.jpg"))
dollar = pygame.image.load(os.path.join("assets", "dollar.png"))
monobg = pygame.image.load(os.path.join("assets", "monobg.jpg"))
endscreen = pygame.image.load(os.path.join("assets", "endscreen.jpg"))
scorecard = pygame.image.load(os.path.join("assets", "score.JPEG"))
highscorecard = pygame.image.load(os.path.join("assets", "highscore.JPEG"))
housecard = pygame.image.load(os.path.join("assets", "houses.JPEG"))
hotelcard = pygame.image.load(os.path.join("assets", "hotels.JPEG"))
boardwalk = pygame.image.load(os.path.join("assets", "boardwalk.JPEG"))
thankyou = pygame.image.load(os.path.join("assets", "thankyou.JPEG"))
gamemap = pygame.transform.scale(gamemap,(450,450))
blackground = pygame.transform.scale(blackground,(dim_field))
monobg = pygame.transform.scale(monobg,dim_field)
endscreen = pygame.transform.scale(endscreen,dim_field)
boardwalk = pygame.transform.scale(boardwalk,dim_field)
thankyou = pygame.transform.scale(thankyou,dim_field)
#SPRITES
monorect = pygame.Rect(240,300,24,26)
policerect1 = pygame.Rect(220,252,16,26)
policerect2 = pygame.Rect(235,252,16,26)
policerect3 = pygame.Rect(250,252,16,26)
policerect4 = pygame.Rect(265,252,16,26)

monopoly = pygame.transform.scale(monopoly,(24,26))
monopoly2 = pygame.transform.scale(monopoly2,(24,26))
monopolyflip = pygame.transform.scale(monopolyflip,(24,26))
monopolyflip2 = pygame.transform.scale(monopolyflip2,(24,26))

police = pygame.transform.scale(police, (16,26))
policewalk = pygame.transform.scale(policewalk, (16,26))
dollar = pygame.transform.scale(dollar,(15,15))
scorecard = pygame.transform.scale(scorecard,(100,114))
highscorecard = pygame.transform.scale(highscorecard,(100,114))
housecard = pygame.transform.scale(housecard,(100,114))
hotelcard = pygame.transform.scale(hotelcard,(100,114))
police_list = [policerect1, policerect2, policerect3, policerect4]

px1 = 0
py1 = 0
px2 = 0
py2 = 0
px3 = 0
py3 = 0
px4 = 0
py4 = 0

x = 85
y = 450
w = 15
h = 15

x1 = 25
y1 = 258
w1 = 15
h1 = 15

scorerect = pygame.Rect(26,515,114,105)
highscorerect = pygame.Rect(142,515,114,105)
housecardrect = pygame.Rect(258,515,114,105)
hotelcardrect = pygame.Rect(374,515,114,105)

#MAZE
highscorelist = [0]



clock = pygame.time.Clock()
FPS = 60
running = True
starting = True
gaming = True
ending = True
winning = True
i = 0
j = 0
houses = 0
hotels = 0
score = 0
policewalking = 0
policewalking2 = 0
policewalking3 = 0
policewalking4 = 0

podirect1 = random.randint(1,4)
podirect2 = random.randint(1,4)
podirect3 = random.randint(1,4)
podirect4 = random.randint(1,4)

# policerect = [policerect1,policerect2,policerect3,policerect4]
police1x = policerect1.left
police1y = policerect1.top
police2x = policerect2.left
police2y = policerect2.top
police3x = policerect3.left
police3y = policerect3.top
police4x = policerect4.left
police4y = policerect4.top
poxcoor = [police1x,police2x,police3x,police4x]
poycoor = [police1y,police2y,police3y,police4y]
policedirect = [podirect1,podirect2,podirect3,podirect4]
px = [px1,px2,px3,px4]
py = [py1,py2,py3,py4]
policeid1 = 0
policeid2 = 0
policeid3 = 0
policeid4 = 0
poindex = [policeid1,policeid2,policeid3,policeid4]
monolist = [monorect]

while running:
  # starting = True
  gaming = True
  ending = True
  monorect.x = 240
  monorect.y = 300
  policerect1.x = 220
  policerect1.y = 252
  policerect2.x = 235
  policerect2.y = 252
  policerect3.x = 250
  policerect3.y = 252
  policerect4.x = 265
  policerect4.y = 252
  
  i = 0
  j = 0
  policewalking = 0
  policewalking2 = 0
  policewalking3 = 0
  policewalking4 = 0
  score = 0
  houses = 0
  hotels = 0
  step_x = 0
  step_y = 0
  # score = 0
  px1 = 0
  py1 = 0
  px2 = 0
  py2 = 0
  px3 = 0
  py3 = 0
  px4 = 0
  py4 = 0
  dollarrect10 = pygame.Rect(x1,y1,w1,h1)
  dollarrect11 = pygame.Rect(x1+30,y1,w1,h1)
  dollarrect12 = pygame.Rect(x1+60,y1,w1,h1)
  dollarrect13 = pygame.Rect(x1+90,y1,w1,h1)
  dollarrect14 = pygame.Rect(x1+120,y1,w1,h1)
  dollarrect15 = pygame.Rect(x1+120,y1-30,w1,h1)
  dollarrect16 = pygame.Rect(x1+120,y1-60,w1,h1)
  dollarrect17 = pygame.Rect(x1+120,y1-90,w1,h1)
  dollarrect18 = pygame.Rect(x1+120,y1-120,w1,h1)
  dollarrect19 = pygame.Rect(x1+120,y1-150,w1,h1)
  dollarrect20 = pygame.Rect(x1+90,y1-150,w1,h1)
  dollarrect21 = pygame.Rect(x1+60,y1-150,w1,h1)
  dollarrect22 = pygame.Rect(x1+30,y1-145,w1,h1)
  dollarrect23 = pygame.Rect(x1+30,y1-165,w1,h1)
  dollarrect24 = pygame.Rect(x1+30,y1-190,w1,h1)
  dollarrect25 = pygame.Rect(x1+60,y1-190,w1,h1)
  dollarrect26 = pygame.Rect(x1+90,y1-190,w1,h1)
  dollarrect27 = pygame.Rect(x1+120,y1-190,w1,h1)
  dollarrect28 = pygame.Rect(x1+150,y1-190,w1,h1)
  dollarrect29 = pygame.Rect(x1+180,y1-190,w1,h1)
  dollarrect30 = pygame.Rect(x1+180,y1-165,w1,h1)
  dollarrect31 = pygame.Rect(x1+180,y1-135,w1,h1)
  dollarrect32 = pygame.Rect(x1+180,y1-105,w1,h1)
  dollarrect33 = pygame.Rect(x1+180,y1-75,w1,h1)
  dollarrect34 = pygame.Rect(x1+180,y1-45,w1,h1)

  dollarrect35 = pygame.Rect(x1+30,y1-120,w1,h1)
  dollarrect36 = pygame.Rect(x1+30,y1-90,w1,h1)
  dollarrect37 = pygame.Rect(x1+60,y1-90,w1,h1)
  dollarrect38 = pygame.Rect(x1+90,y1-90,w1,h1)

  dollarrect39 = pygame.Rect(x1+210,y1-45,w1,h1)
  dollarrect40 = pygame.Rect(x1+240,y1-45,w1,h1)
  dollarrect41 = pygame.Rect(x1+240,y1-75,w1,h1)
  dollarrect42 = pygame.Rect(x1+240,y1-105,w1,h1)
  dollarrect43 = pygame.Rect(x1+240,y1-135,w1,h1)
  dollarrect44 = pygame.Rect(x1+240,y1-165,w1,h1)
  dollarrect45 = pygame.Rect(x1+240,y1-190,w1,h1)
  dollarrect46 = pygame.Rect(x1+270,y1-190,w1,h1)
  dollarrect47 = pygame.Rect(x1+300,y1-190,w1,h1)
  dollarrect48 = pygame.Rect(x1+330,y1-190,w1,h1)
  dollarrect49 = pygame.Rect(x1+370,y1-190,w1,h1)
  dollarrect50 = pygame.Rect(x1+405,y1-190,w1,h1)
  dollarrect51 = pygame.Rect(x1+405,y1-165,w1,h1)
  dollarrect52 = pygame.Rect(x1+405,y1-145,w1,h1)
  dollarrect53 = pygame.Rect(x1+405,y1-120,w1,h1)
  dollarrect54 = pygame.Rect(x1+405,y1-90,w1,h1)

  dollarrect55 = pygame.Rect(x1+375,y1-150,w1,h1)
  dollarrect56 = pygame.Rect(x1+345,y1-150,w1,h1)
  dollarrect57 = pygame.Rect(x1+315,y1-150,w1,h1)
  dollarrect58 = pygame.Rect(x1+315,y1-120,w1,h1)
  dollarrect59 = pygame.Rect(x1+315,y1-90,w1,h1)
  dollarrect60 = pygame.Rect(x1+315,y1-60,w1,h1)
  dollarrect61 = pygame.Rect(x1+315,y1-30,w1,h1)
  dollarrect62 = pygame.Rect(x1+315,y1,w1,h1)
  dollarrect63 = pygame.Rect(x1+345,y1,w1,h1)
  dollarrect64 = pygame.Rect(x1+375,y1,w1,h1)
  dollarrect65 = pygame.Rect(x1+405,y1,w1,h1)
  dollarrect66 = pygame.Rect(x1+435,y1,w1,h1)
  dollarrect67 = pygame.Rect(x1+375,y1-90,w1,h1)
  dollarrect68 = pygame.Rect(x1+345,y1-90,w1,h1)

  dollarrect69 = pygame.Rect(x1+315,y1+30,w1,h1)
  dollarrect70 = pygame.Rect(x1+315,y1+60,w1,h1)
  dollarrect71 = pygame.Rect(x1+315,y1+90,w1,h1)
  dollarrect72 = pygame.Rect(x1+355,y1+120,w1,h1)
  dollarrect73 = pygame.Rect(x1+355,y1+145,w1,h1)

  dollarrect1 = pygame.Rect(x1+120,y1+30,w1,h1)
  dollarrect2 = pygame.Rect(x1+120,y1+60,w1,h1)
  dollarrect3 = pygame.Rect(x1+120,y1+90,w1,h1)
  dollarrect4 = pygame.Rect(x1+90,y1+120,w1,h1)
  dollarrect5 = pygame.Rect(x1+90,y1+145,w1,h1)


  dollarrect6 = pygame.Rect(x1+90,y1+90,w1,h1)
  dollarrect7 = pygame.Rect(x1+60,y1+90,w1,h1)
  dollarrect8 = pygame.Rect(x1+30,y1+90,w1,h1)
  dollarrect9 = pygame.Rect(x1+30,y1+120,w1,h1)

  dollarrect74 = pygame.Rect(x1+30,y1+150,w1,h1)
  dollarrect75 = pygame.Rect(x1+30,y1+180,w1,h1)
  dollarrect76 = pygame.Rect(x1+30,y1+205,w1,h1)

  dollarrect77 = pygame.Rect(x1+60,y1+205,w1,h1)
  dollarrect78 = pygame.Rect(x1+90,y1+205,w1,h1)
  dollarrect79 = pygame.Rect(x1+120,y1+205,w1,h1)
  dollarrect80 = pygame.Rect(x1+150,y1+205,w1,h1)
  dollarrect81 = pygame.Rect(x1+180,y1+205,w1,h1)
  dollarrect82 = pygame.Rect(x1+210,y1+205,w1,h1)
  dollarrect83 = pygame.Rect(x1+240,y1+205,w1,h1)
  dollarrect84 = pygame.Rect(x1+270,y1+205,w1,h1)
  dollarrect85 = pygame.Rect(x1+300,y1+205,w1,h1)
  dollarrect86 = pygame.Rect(x1+330,y1+205,w1,h1)
  dollarrect87 = pygame.Rect(x1+360,y1+205,w1,h1)
  dollarrect88 = pygame.Rect(x1+390,y1+205,w1,h1)
  dollarrect89 = pygame.Rect(x1+415,y1+205,w1,h1)

  dollarrect90 = pygame.Rect(x1+415,y1+175,w1,h1)
  dollarrect91 = pygame.Rect(x1+415,y1+145,w1,h1)
  dollarrect92 = pygame.Rect(x1+415,y1+115,w1,h1)
  dollarrect93 = pygame.Rect(x1+415,y1+85,w1,h1)
  dollarrect94 = pygame.Rect(x1+385,y1+85,w1,h1)
  dollarrect95 = pygame.Rect(x1+355,y1+85,w1,h1)
  dollarrect96 = pygame.Rect(x1+180,y1+170,w1,h1)
  dollarrect97 = pygame.Rect(x1+180,y1+145,w1,h1)
  dollarrect98 = pygame.Rect(x1+180,y1+120,w1,h1)
  dollarrect99 = pygame.Rect(x1+180,y1+90,w1,h1)
  
  dollarrect100 = pygame.Rect(x1+90,y1+170,w1,h1)
  dollarrect101 = pygame.Rect(x1+150,y1+90,w1,h1)
  dollarrect102 = pygame.Rect(x1+120,y1+170,w1,h1)
  dollarrect103 = pygame.Rect(x1+150,y1+170,w1,h1)

  dollarrect104 = pygame.Rect(x1+355,y1+165,w1,h1)
  dollarrect105 = pygame.Rect(x1+245,y1+165,w1,h1)
  dollarrect106 = pygame.Rect(x1+245,y1+140,w1,h1)
  dollarrect107 = pygame.Rect(x1+245,y1+115,w1,h1)
  dollarrect108 = pygame.Rect(x1+245,y1+90,w1,h1)
  dollarrect109 = pygame.Rect(x1+275,y1+90,w1,h1)
  dollarrect110 = pygame.Rect(x1+275,y1+165,w1,h1)
  dollarrect111 = pygame.Rect(x1+305,y1+165,w1,h1)
  dollarrect112 = pygame.Rect(x1+330,y1+165,w1,h1)








  dollar_list = [dollarrect1, dollarrect2,dollarrect3,dollarrect4,dollarrect5,dollarrect6, dollarrect7, dollarrect8, dollarrect9, dollarrect10,dollarrect11,dollarrect12,dollarrect13,dollarrect14,dollarrect15,dollarrect16,dollarrect17,dollarrect18,dollarrect19,dollarrect20, dollarrect21,dollarrect22,dollarrect23,dollarrect24,dollarrect25,dollarrect26,dollarrect27,dollarrect28,dollarrect29,dollarrect30,dollarrect31,dollarrect32,dollarrect33,dollarrect34,dollarrect35, dollarrect36,dollarrect37,dollarrect38,dollarrect39,dollarrect40,dollarrect41,dollarrect42,dollarrect43,dollarrect44,dollarrect45,dollarrect46,dollarrect47,dollarrect48,dollarrect49,dollarrect50,dollarrect51,dollarrect52,dollarrect53,dollarrect54,dollarrect55,dollarrect56,dollarrect57,dollarrect58,dollarrect59,dollarrect60,dollarrect61,dollarrect62,dollarrect63,dollarrect64,dollarrect65,dollarrect66,dollarrect67,dollarrect68,dollarrect69,dollarrect70,dollarrect71,dollarrect72,dollarrect73,dollarrect74,dollarrect75,dollarrect76,dollarrect77,dollarrect78,dollarrect79,dollarrect80,dollarrect81,dollarrect82,dollarrect83,dollarrect84,dollarrect85,dollarrect86,dollarrect87,dollarrect88,dollarrect89,dollarrect90,dollarrect91,dollarrect92,dollarrect93,dollarrect94,dollarrect95,dollarrect96,dollarrect97,dollarrect98,dollarrect99,dollarrect100,dollarrect101,dollarrect102,dollarrect103,dollarrect104, dollarrect105,dollarrect106,dollarrect107,dollarrect108,dollarrect109,dollarrect110,dollarrect111,dollarrect112] 
   
  while starting:
    screen.blit(monobg, (0,0))
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          starting = False
    pygame.display.update()
  while gaming:

    clock.tick(FPS)
    
    
    
 
    xcoor = monorect.left
    ycoor = monorect.top
    if score == 154:
      gaming == False
      break
    
    ind = monorect.collidelist(rect_list)  
    if not ind == -1 and step_x == 1:
      monorect = pygame.Rect(xcoor-1,ycoor,24,26)
    elif not ind == -1 and step_x == -1:
      monorect = pygame.Rect(xcoor+1,ycoor,24,26)
    elif not ind == -1 and step_y == 1:
      monorect = pygame.Rect(xcoor,ycoor-1,24,26)
    elif not ind == -1 and step_y == -1:
      monorect = pygame.Rect(xcoor,ycoor+1,24,26)
    else: 
      pass
    

    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          step_x = 1
          step_y = 0
        if event.key == pygame.K_LEFT:
          step_x = -1
          step_y = 0
        if event.key == pygame.K_UP:
          step_y = -1
          step_x = 0
        if event.key == pygame.K_DOWN:
          step_y = 1
          step_x = 0
        # if event.key == pygame.K_q and xcoor > 180 and >280 and ycoor > 240 and ycoor < 280:
        #   score += 1
          
      

    monorect.move_ip(step_x,step_y)
   
    if xcoor == 25 and step_x == -1:
      monorect.x = 451
    elif xcoor == 451 and step_x == 1:
      monorect.x = 25
    else:
      pass
      
    screen.blit(blackground, (0,0))
    # screen.blit(gamemap, (25,40))
    for qwer in range(len(walls)):
        pygame.draw.rect(screen,mazecolor,walls[qwer])
    # pygame.draw.rect(gamemap,mazecolor,mazerect1)
    # pygame.draw.rect(gamemap,mazecolor,mazerect1b)
    if i%90 >= 45 and not step_x == -1:
      screen.blit(monopoly,monorect)
    elif i%90 < 45 and not step_x == -1:
      screen.blit(monopoly2,monorect)
    elif i%90 >= 45 and step_x == -1:
      screen.blit(monopolyflip,monorect)
    elif i%90 < 45 and step_x == -1:
      screen.blit(monopolyflip2,monorect)

    
    
    
    ###POLICE
    police1x = policerect1.left
    police1y = policerect1.top
    police2x = policerect2.left
    police2y = policerect2.top
    police3x = policerect3.left
    police3y = policerect3.top
    police4x = policerect4.left
    police4y = policerect4.top
    
    policeid1 = policerect1.collidelist(rect_list)
    policeid2 = policerect2.collidelist(rect_list)
    policeid3 = policerect3.collidelist(rect_list)
    policeid4 = policerect4.collidelist(rect_list)

    if not policeid1 == -1 and px1 == 1:
      px1 = 0
      py1 = random.choice([-1,1])
      policerect1.move_ip(-1,0)
    elif not policeid1 == -1 and px1 == -1:
      px1 = 0
      py1 = random.choice([-1,1])
      policerect1.move_ip(1,0)
    elif not policeid1 == -1 and py1 == 1:
      px1 = random.choice([-1,1])
      py1 = 0
      policerect1.move_ip(0,-1)
    elif not policeid1 == -1 and py1 == -1:
      px1 = random.choice([-1,1])
      py1 = 0
      policerect1.move_ip(0,1)
    
    if not policeid2 == -1 and px2 == 1:
      px2 = 0
      py2 = random.choice([-1,1])
      policerect2.move_ip(-1,0)
    elif not policeid2 == -1 and px2 == -1:
      px2 = 0
      py2 = random.choice([-1,1])
      policerect2.move_ip(1,0)
    elif not policeid2 == -1 and py2 == 1:
      px2 = random.choice([-1,1])
      py2 = 0
      policerect2.move_ip(0,-1)
    elif not policeid2 == -1 and py2 == -1:
      px2 = random.choice([-1,1])
      py2 = 0
      policerect2.move_ip(0,1)

    if not policeid3 == -1 and px3 == 1:
      px3 = 0
      py3 = random.choice([-1,1])
      policerect3.move_ip(-1,0)
    elif not policeid3 == -1 and px3 == -1:
      px3 = 0
      py3 = random.choice([-1,1])
      policerect3.move_ip(1,0)
    elif not policeid3 == -1 and py3 == 1:
      px3 = random.choice([-1,1])
      py3 = 0
      policerect3.move_ip(0,-1)
    elif not policeid3 == -1 and py3 == -1:
      px3 = random.choice([-1,1])
      py3 = 0
      policerect3.move_ip(0,1)

    if not policeid4 == -1 and px4 == 1:
      px4 = 0
      py4 = random.choice([-1,1])
      policerect4.move_ip(-1,0)
    elif not policeid4 == -1 and px4 == -1:
      px4 = 0
      py4 = random.choice([-1,1])
      policerect4.move_ip(1,0)
    elif not policeid4 == -1 and py4 == 1:
      px4 = random.choice([-1,1])
      py4 = 0
      policerect4.move_ip(0,-1)
    elif not policeid4 == -1 and py4 == -1:
      px4 = random.choice([-1,1])
      py4 = 0
      policerect4.move_ip(0,1)

    

    # if i > 200:
    #   if policewalking < 50:
    #     if podirect1 == 1:
    #       px1 = 0
    #       py1 = 1
    #     elif podirect1 == 2:
    #       px1 = 0
    #       py1 = -1
    #     elif podirect1 == 3:
    #       px1 = 1
    #       py1 = 0
    #     else:
    #       px1 = -1
    #       py1 = 0

    #     policewalking += 1
    #   else:
    #     policewalking = 0
    #     podirect1 = random.randint(1,4)
    policerect1.move_ip(px1,py1)


    # if i > 55:
    #   if policewalking2 < 50:
    #     if podirect2 == 1:
    #       px2 = 0
    #       py2 = 1
    #     elif podirect1 == 2:
    #       px2 = 0
    #       py2 = -1
    #     elif podirect1 == 3:
    #       px2 = 1
    #       py2 = 0
    #     else:
    #       px2 = -1
    #       py2 = 0

    #   policewalking2 += 1
    # else:
    #   policewalking2 = 0
    #   podirect2 = random.randint(1,4)
    policerect2.move_ip(px2,py2)
    
    # if i > 115:
    #   if policewalking3 < 50:
    #     if podirect3 == 1:
    #       px3 = 0
    #       py3 = 1
    #     elif podirect1 == 2:
    #       px3 = 0
    #       py3 = -1
    #     elif podirect1 == 3:
    #       px3 = 1
    #       py3 = 0
    #     else:
    #       px3 = -1
    #       py3 = 0

    #     policewalking3 += 1
    #   else:
    #     policewalking = 0
    #     podirect3 = random.randint(1,4)
    policerect3.move_ip(px3,py3)

    # if i > 280:
    #   if policewalking4 < 50:
    #     if podirect1 == 1:
    #       px4 = 0
    #       py4 = 1
    #     elif podirect4 == 2:
    #       px4 = 0
    #       py4 = -1
    #     elif podirect4 == 3:
    #       px4 = 1
    #       py4 = 0
    #     else:
    #       px4 = -1
    #       py4 = 0

    #     policewalking4 += 1
    #   else:
    #     policewalking4 = 0
    #     podirect4 = random.randint(1,4)
    policerect4.move_ip(px4,py4)
    print(policeid1)
    if i < 10:
      # policerect2.move_ip(1,0)
      px2 = 1
      py2 = 0

    elif i > 10 and i < 60:
      # policerect2.move_ip(0,-1)
      px2 = 0
      py2 = -1
      
    elif i < 70 and i > 65:
      # policerect3.move_ip(-1,0)
      px3 = -1
      py3 = 0

    elif i > 70 and i < 120:
      # policerect3.move_ip(0,-1) 
      px3 = 0
      py3 = -1         

    elif i < 155 and i > 135:
      # policerect1.move_ip(1,0)
      px1 = 1
      py1 = 0

    elif i > 155 and i < 205:
      # policerect1.move_ip(0,-1)
      px1 = 0
      py1 = -1

    elif i < 235 and i > 215:
      # policerect4.move_ip(-1,0)
      px4 = -1
      py4 = 0

    elif i > 235 and i < 285:
      # policerect4.move_ip(0,-1)
      px4 = 0
      py4 = -1


    
    index = monorect.collidelist(police_list)
    # poind1 = policerect1.collidelist(monolist)
    # poind2 = policerect2.collidelist(monolist)
    # poind3 = policerect3.collidelist(monolist)
    # poind4 = policerect4.collidelist(monolist)
    # print(index)
    if not index == -1:
      gaming = False
      break



    if i%90 >= 45:
      screen.blit(police,policerect1)
      screen.blit(police,policerect2)
      screen.blit(police,policerect3)
      screen.blit(police,policerect4)
    else:
      screen.blit(policewalk,policerect1)
      screen.blit(policewalk,policerect2)
      screen.blit(policewalk,policerect3)
      screen.blit(policewalk,policerect4)
    
    i += 1
    
    




    



    if i%500 == 0:
      mazecolor = colorlist[j]
      j+=1
    else:
      pass
    if j > 3:
      j = 0

    scoreid = monorect.collidelist(dollar_list)
    
    if not scoreid == -1:
      score += 1
      dollar_list[scoreid] = pygame.Rect(-100,-100,w,h)
      # print(scoreid)
    
    
    if score%10 == 0 and not score == 0:
      houses += 1
      score += 2
    else:
      pass
    
    if houses == 4:
      hotels += 1
      houses = 0
      score += 4
    else:
      pass

      
    # print(score)
    highscorelist.append(score)
    highscore = max(highscorelist)
    # print(highscore)
    for k in range(len(dollar_list)):
      screen.blit(dollar,dollar_list[k])
    # print(ind)
    screen.blit(scorecard,scorerect)
    screen.blit(highscorecard,highscorerect)
    screen.blit(housecard,housecardrect)
    screen.blit(hotelcard,hotelcardrect)
    
    #ONLY CODE COPIED (5 LINES)
    pygame.font.init() 
    myfont = pygame.font.SysFont('Comic Sans MS', 64)
    showscore = myfont.render(str(score), False, (0,0,0))
    showhighscore = myfont.render(str(highscore),False,(0,0,0))
    showhouse = myfont.render(str(houses), False, (0,0,0))
    showhotel = myfont.render(str(hotels), False, (0,0,0))
    screen.blit(showscore,(50,560))
    screen.blit(showhighscore,(165,565))
    screen.blit(showhouse,(295,560))
    screen.blit(showhotel,(410,560))
    
    
    pygame.display.update()
  
  if not score == 154:

    while ending:
      screen.blit(endscreen, (0,0))
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_1:
            ending = False
          if event.key == pygame.K_2:
            screen.blit(thankyou,(0,0))
            running = False
            ending = False
      pygame.display.update()
  
  else:

    while winning:
      screen.blit(boardwalk, (0,0))
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_1:
            winning = False
          if event.key == pygame.K_2:
            screen.blit(thankyou,(0,0))
            running = False
            winning = False
      pygame.display.update()
  
  
  
  pygame.display.update() 

# fontfont = pygame.font.SysFont('Comic Sans MS', 96)
# thankyou = fontfont.render("Thank you for playing!", False, (255,255,255))
# screen.blit(thankyou,(185,325))