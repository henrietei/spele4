import pygame
import sys


black = (0,0,0)
white = (255, 255, 255)
gray = (230, 230, 230)
gray1 = (220, 220, 220)
yellow = (255, 255, 0)
green = (0, 255, 0)  

yellow_letters=[]
green_letters=[]

a="bumba"

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
                print(letter, i)
                correct_letters += 1
                green_letters.append(i)
            else:
                print(letter, "/", i)
                yellow_letters.append(i)
                
            #a1_copy.remove(letter)
            a1.remove(letter)
        else:
            print(letter)

    if correct_letters == 5:
        print("pareizs vards")


def letter_colors():
    for index in green_letters:
        pygame.draw.rect(screen, green, (100+index*85, 105+100*k, 60, 90))

    for index1 in yellow_letters:
        pygame.draw.rect(screen, yellow, (100+index1*85, 105+100*k, 60, 90))
        

pygame.init()
  
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 800])
base_font = pygame.font.Font("SourceCodePro-ExtraBold.ttf", 72)
user_text = ''
w_font=pygame.font.Font("SourceCodePro-ExtraBold.ttf", 28)

screen.fill(gray)
surface1()


for k in range(6):
    input_rect = pygame.Rect(100, 95+k*100, 225, 72)
    #pygame.draw.rect(screen, white, input_rect)
    z=0
 
    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RETURN:
                    if len(user_text)==10:
                        minejums=user_text.replace(" ", "")
                        print(minejums)
                        pygame.draw.rect(screen, gray, (0, 0, 600, 100))
                        z=1
                        check_letters()
                        letter_colors()
                        
                    else: 
                        warning = w_font.render("Nepietiekami daudz burtu", True, black)
                        screen.blit(warning,(100, 60))
                        #time.sleep(2)
                        
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-2]
                    
                else:
                    if len(user_text)<=9:
                        if ord(event.unicode)>65:
                            user_text += event.unicode + " " 
        

        #screen.fill(gray)
        txtsurf = base_font.render(user_text, True, black)
        screen.blit(txtsurf,(105, 100+100*k))
        pygame.display.flip()
        
        clock.tick(60)
        
        if z==1:
            user_text=""
            correct_letters=[]
            yellow_letters=[]
            green_letters=[]
            break




        
        
