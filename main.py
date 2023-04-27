import pygame
import sys
import random
#import ptext


black = (0,0,0)
white = (255, 255, 255)
gray = (230, 230, 230)
gray1 = (220, 220, 220)
yellow = (255, 255, 0)
green = (0, 255, 0)  
red = (255, 0, 0)
blue = (173, 216, 230)

yellow_letters=[]
green_letters=[]
correct_letters=0
"""
tutorial_text1=[("Vārdu minēšanas spēle
Jūsu uzdevums ir atminēt piecu burtu vārdu.
Ja burta lauciņš iekrāsojas dzeltenā krāsā, tas nozīmē, ka burts ir vārdā, bet neīstajā vietā. 
Ja burta lauciņš iekrāsojas zaļā krāsā, tas nozīmē, ka burts atrodas īstajā vietā. 
Jūsu rīcībā ir 6 mēģinājumi atminēt vārdu.")]"""

won=False



with open('words.txt', 'r',  encoding="utf-8") as g:
    lines = g.readlines()

b = random.randint(0, len(lines)-1)
a = lines[b]
#print(a)

word="vārds:"+" "+(str(a)[:5])

def tutorial():
    screen.fill(gray)
    tutorial_text= "ashfskf"

    screen.blit(tutorial_text,(520, 100))


def win():
    winner = w_font.render("Jūs uzvarējāt!", True, black)
    screen.blit(winner,(520, 100))


def lose():
    loser = z_font.render("Par daudz", True, black)
    loser1 = z_font.render("mēģinājumu", True, black)
    correct_word = w_font.render(word, True, black)
    screen.blit(loser,(540, 100))
    screen.blit(loser1,(530, 150))
    screen.blit(correct_word,(530, 200))

def surface1():
    for i in range (5):
        for i1 in range (6):
            pygame.draw.rect(screen, gray1, (100+i*85, 105+100*i1, 60, 90))

def check_letters():
    a1 = list(a)
    #a1_copy = a1.copy()
    correct_letters = 0
    for i, letter in enumerate(minejums):
        #if letter in a1_copy:
        if letter in a1:
            if letter == a[i]:
                #print(letter, i)
                correct_letters += 1
                green_letters.append(i)
            else:
                #print(letter, "/", i)
                yellow_letters.append(i)
                
            #a1_copy.remove(letter)
            a1.remove(letter)
        #else:
            #print(letter)

def letter_colors():
    for index in green_letters:
        pygame.draw.rect(screen, green, (100+index*85, 105+100*k, 60, 90))

    for index1 in yellow_letters:
        pygame.draw.rect(screen, yellow, (100+index1*85, 105+100*k, 60, 90))


pygame.init()
  

clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 800])
base_font = pygame.font.Font("SourceCodePro-ExtraBold.ttf", 72)
user_text = ''
w_font=pygame.font.Font("SourceCodePro-ExtraBold.ttf", 28)
z_font=pygame.font.Font("SourceCodePro-ExtraBold.ttf", 36)


screen.fill(gray)
surface1()
user_text=(a[:1])+" "
pygame.draw.rect(screen, green, (100, 105, 60, 90))

won=False
for k in range(7): 
    pygame.draw.rect(screen, gray, (540, 300, 200, 50))
    input_rect = pygame.Rect(100, 95+k*100, 225, 72)
    #pygame.draw.rect(screen, white, input_rect)
    attempts="minējumi:"+/n+str(k)
    attempt = w_font.render(attempts, True, black)
    screen.blit(attempt,(550, 300))

    guess=False

    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RETURN:
                    if len(user_text)==10:
                        minejums=user_text.replace(" ", "")
                        #print(minejums)
                        pygame.draw.rect(screen, gray, (0, 0, 600, 100))
                        guess=True
                        check_letters()
                        letter_colors()
                        if (len(green_letters))==5:
                            won=True
                            win()

                    else: 
                        warning = w_font.render("Nepietiekami daudz burtu", True, black)
                        screen.blit(warning,(100, 60))
                        #time.sleep(2)
                        
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-2]
                    pygame.draw.rect(screen, gray1, (100+(len(user_text))*42.5, 105+100*k, 60, 90))
                    
                else:
                    if len(user_text)<=9:
                        if ord(event.unicode)>65:
                            if won==False:
                                user_text += event.unicode + " " 

        #screen.fill(gray)
        txtsurf = base_font.render(user_text, True, black)
        screen.blit(txtsurf,(105, 100+100*k))
        pygame.display.flip()
        
        clock.tick(60)
        
        if guess==True:
            user_text=""
            #correct_letters=0
            yellow_letters=[]
            green_letters=[]
            break
    if k==5:
        won=True
        lose()

        

        
    






        
        
