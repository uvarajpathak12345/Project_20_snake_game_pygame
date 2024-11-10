import pygame
import random
from pygame import mixer
import menu

pygame.init()

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

direction =(7,0)
count = 0


game_state = False



mixer.music.load("./sound/background.mp3")
mixer.music.play(-1)



class body(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((17,17))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(topleft = (x,y))





class snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.collection = [body(screen_width//2,screen_height//2)]
    

    def move(self):
        new_X = self.collection[0].rect.x + direction[0]
        new_y = self.collection[0].rect.y + direction[1]

        for i in range(len(self.collection)-1,0,-1):
            self.collection[i].rect.topleft = self.collection[i-1].rect.topleft
        

        self.collection[0].rect.topleft = (new_X,new_y)


        if self.collection[0].rect.x > screen_width:
            self.collection[0].rect.x = 0
        elif self.collection[0].rect.x < 0 :
            self.collection[0].rect.x = screen_width
        elif self.collection[0].rect.y > screen_height:
            self.collection[0].rect.y = 0
        elif self.collection[0].rect.y < 0:
            self.collection[0].rect.y = screen_height



    def grow(self):
        tail = self.collection[-1]
        new_body = body(tail.rect.x,tail.rect.y)
        self.collection.append(new_body)

    def score(self):
        score_text = pygame.font.Font("./font.ttf",30)
        score_text_x = 3
        score_text_y = 3
        text = score_text.render(f"Score {count}", True,(0,0,0))
        screen.blit(text,(score_text_x,score_text_y))
    


        
        


class food(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.x,self.y))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(topleft = (screen_width//4,screen_height//4))

    def revieve(self):
        self.rect.topleft = (random.randint(10,600) , random.randint(10,600))





snake_body = snake()
foods = food(17,17)


text = menu.Font("Play", (screen_width // 2 - 60),( screen_height // 2 - 30))

group = pygame.sprite.Group()
group.add(foods)





for bodies in  snake_body.collection:
    group.add(bodies)




run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != (7,0):
                direction = (-7,0)
            elif event.key == pygame.K_RIGHT and direction != (-7,0):
                direction = (7,0)
            elif event.key == pygame.K_UP and direction != (0,7):
                direction = (0,-7)
            elif event.key == pygame.K_DOWN and direction != (0,-7):
                direction = (0,7)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_X,mouse_y = pygame.mouse.get_pos()
            if text.is_clicked((mouse_X,mouse_y)):
                text.clear_text()
                game_state = True

               






    #collosion detection with food
    if pygame.sprite.collide_rect(snake_body.collection[0],foods):
        eat_sound = mixer.Sound("./sound/eat.mp3")
        eat_sound.play()
        foods.revieve()
        snake_body.grow()
        group.add(snake_body.collection[-1])
        count += 1


    
    


    screen.fill((230,100,230))
    text.render(screen)
    
    if game_state:
        group.draw(screen)
        snake_body.move()
        snake_body.score()



    pygame.display.update()
    clock.tick(60)
pygame.quit()
    