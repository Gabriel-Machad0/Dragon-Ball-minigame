import os
import pygame
from sys import exit
from random import randint



# "Turning on Pygame", and creating the screen that the game will be played on
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Dragon Ball Mini Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)


# Loading Background Images
kamehouse = pygame.image.load(os.path.join("background","kamehouse.png")).convert()
ground = pygame.image.load(os.path.join("background","ground.png")).convert()
gameoverBG = pygame.image.load(os.path.join("background","gokucrying.jpeg")).convert()
gameoverBG = pygame.transform.scale(gameoverBG , (600,500))
initial_screen = pygame.image.load(os.path.join("background","DragonBallZ initial.jpeg")).convert()
initial_screen = pygame.transform.scale(initial_screen , (600,500))

# Score text
score_surface = test_font.render("Dragon Ball Z", True, (64,64,64))
score_rect = score_surface.get_rect(midbottom = (300,100))



# Background sprite colors
BLUE = (0, 123, 132)
GREEN = (2, 128, 109)









# Scoring

start_time = 0

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(str(current_time), False, (64,64,64))
    score_rect = score_surf.get_rect(center = (300,50))
    screen.blit(score_surf,score_rect)

    return current_time

score = 0


#def obstacle_movement 

# Game variables
game_active = True 

game_name = test_font.render("Dragon Ball Runner", False, ("Yellow"))
game_name_rect = game_name.get_rect(center = (300,50))

game_message = test_font.render("Press Space To Run", False, "Black")
game_message_rect = game_message.get_rect(center = (300,460
))



#___________________________________________TIMER___________________________________________________


obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

#__________________________________BACKGROUND SPRITE COLORS________________________________________

GOKU_BLUE = (0, 123, 132)
CELLJR_GREEN = (2, 128, 109)
CAPGINYU_GREEN = (0, 132, 107)



# Function to get single sprite out of sprite sheet

def get_image(sheet, frame, width, height, yaxis, scale, colour):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), yaxis, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colour)


    return image



#GOKU
goku_sprites = pygame.image.load(os.path.join("SpritesDB","Goku (1).gif")).convert_alpha()

#Frames
goku_frame_0 = get_image(goku_sprites, 0, 48, 55, 20, 1.5, GOKU_BLUE)
goku_frame_1 = get_image(goku_sprites, 1, 48, 55, 20, 1.5, GOKU_BLUE)
goku_frame_2 = get_image(goku_sprites, 2, 48, 55, 20, 1.5, GOKU_BLUE)
goku_frame_3 = get_image(goku_sprites, 3, 48, 55, 20, 1.5, GOKU_BLUE)

#Player rectangle
goku_rect = goku_frame_0.get_rect(midbottom = (25,425))

#Player Gravity
player_gravity = 0







#CELL JR

cell_jr_sprites = pygame.image.load(os.path.join("SpritesDB","Cell Jr.gif")).convert_alpha()

#Frames
cell_frame_0 = get_image(cell_jr_sprites, 0, 42, 45, 0, 1.5, CELLJR_GREEN)
cell_frame_1 = get_image(cell_jr_sprites, 1, 42, 45, 0, 1.5, CELLJR_GREEN)
cell_frame_2 = get_image(cell_jr_sprites, 2, 42, 45, 0, 1.5, CELLJR_GREEN)
cell_frame_3 = get_image(cell_jr_sprites, 3, 42, 45, 0, 1.5, CELLJR_GREEN)

#player rectangle
cell_jr_rect = cell_frame_0.get_rect(bottomright = (600, 425))






# CAPTAIN GINYU

captain_ginyu_sprites = pygame.image.load(os.path.join("SpritesDB","Captain Ginyu.gif")).convert_alpha()

#Frames
cap_ginyu_frame_0 = get_image(captain_ginyu_sprites, 0, 42, 45, 15, 1.5, CAPGINYU_GREEN)
cap_ginyu_frame_1 = get_image(captain_ginyu_sprites, 1, 42, 45, 15, 1.5, CAPGINYU_GREEN)
cap_ginyu_frame_2 = get_image(captain_ginyu_sprites, 2, 42, 45, 15, 1.5, CAPGINYU_GREEN)
cap_ginyu_frame_3 = get_image(captain_ginyu_sprites, 3, 42, 45, 15, 1.5, CAPGINYU_GREEN)

#player rectangle
cap_ginyu_rect = cap_ginyu_frame_0.get_rect(center = (500, 200))


obstacle_rect_list = []

#____________________________________________GAME LOOP________________________________________________



while True:

    # Checking for user input in order to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if goku_rect.collidepoint(event.pos) and goku_rect.bottom >= 425:
                    player_gravity = -15

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and goku_rect.bottom >= 425:
                    player_gravity = -30
                
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True  
                cell_jr_rect.left = 600   
                start_time = int(pygame.time.get_ticks() / 1000)
            
        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(cell_frame_0.get_rect(bottomright = (randint(900,1100), 425))) 
    if game_active:

        #Background images
        screen.blit(kamehouse, (0,0))
        screen.blit(ground, (0,425))
        
        #Score text
        # pygame.draw.rect(screen, "#c0e8ec", score_rect,10)
        # pygame.draw.rect(screen, "#c0e8ec", score_rect)
        # screen.blit(score_surface, score_rect)
        score = display_score()
        


        # GOKU Player
        player_gravity += 1  
        goku_rect.y += player_gravity
        if goku_rect.bottom >= 425:
            goku_rect.bottom = 425
        screen.blit(goku_frame_0, goku_rect)
        


        #Cell JR CPU
        #obstacle_movement(obstacle_rect_list)
        # cell_jr_rect.x -= 4
        # if cell_jr_rect.right <= 0 :
        #     cell_jr_rect.left = 600
        # screen.blit(cell_frame_0, cell_jr_rect)



        screen.blit(cap_ginyu_frame_0, cap_ginyu_rect)





        #COLLISION

        if cell_jr_rect.colliderect(goku_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(initial_screen, (0,0))

        score_message = test_font.render(f"Your score: {score}", False, "Yellow")
        score_message_rect = score_message.get_rect(center = (300,85))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)       
        else:
            screen.blit(score_message,score_message_rect)

     
    



    # Line that updates what shows on the display
    pygame.display.update()

    # Framerate
    clock.tick(60)










