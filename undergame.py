# Example file showing a basic pygame "game loop"
import pygame
import random
# pygame setup
pygame.init()
WIDTH=1000
HEIGHT=800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

RED = pygame.Color(255,0,0)
PURPLE = pygame.Color(150,30,245)
BLACK = pygame.Color(0,0,0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
GREEN = pygame.Color(0,255,0)
YELLOW = pygame.Color(255,255,0)
WHITE = pygame.Color(255,255,255)

font = pygame.font.Font('freesansbold.ttf', 32)


class Player:
    def __init__(self, rectangle, image, speed, game):
        
        self.game=game
        game.allThings.append(rectangle)
        self.rectangle=rectangle
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image, (rectangle.width, rectangle.height))
        self.speed = speed
        self.color=PURPLE
        self.colliding=False
        self.health=50
        self.dead=False

    def collidingWith(self, rect2):
        rect=self.rectangle
        if rect.x<=(rect2.x+rect2.width) and (rect.x+rect.width)>=rect2.x and rect.y<=(rect2.y+rect2.height) and (rect.y+rect.height)>=rect2.y:
            return True
            

    def move_left(self):
        player_box=self.game.player_box
        if self.rectangle.x>player_box.x:
            self.rectangle.x-=self.speed
    def move_right(self):
        player_box=self.game.player_box
        if self.rectangle.x<player_box.x+player_box.width-self.rectangle.width:
            self.rectangle.x+=self.speed
    def move_up(self):
        player_box=self.game.player_box
        if self.rectangle.y>player_box.y:
            self.rectangle.y-=self.speed
    def move_down(self):
        player_box=self.game.player_box
        if self.rectangle.y<player_box.y+player_box.height-self.rectangle.width:
            self.rectangle.y+=self.speed

    def move(self):
        if not self.dead:
            keys_down=pygame.key.get_pressed()

            if keys_down[pygame.K_LEFT]:
                self.move_left()
            if keys_down[pygame.K_RIGHT]:
                self.move_right()
            if keys_down[pygame.K_UP]:
                self.move_up()
            if keys_down[pygame.K_DOWN]:
                self.move_down()

            self.colliding=False
            for r in self.game.allThings:
                if r!=self.rectangle and self.collidingWith(r):
                    self.colliding=True

            for b in self.game.enemy.boxes:
                if self.collidingWith(b.rectangle):
                    self.hit(b)
                    if self.health<=0:
                        self.health=0
                        self.dead=True

    def move2(self):
        if not self.dead:
            keys_down=pygame.key.get_pressed()

            if keys_down[pygame.K_a]:
                self.move_left()
            if keys_down[pygame.K_d]:
                self.move_right()
            if keys_down[pygame.K_w]:
                self.move_up()
            if keys_down[pygame.K_s]:
                self.move_down()

            self.colliding=False
            for r in self.game.allThings:
                if r!=self.rectangle and self.collidingWith(r):
                    self.colliding=True

            for b in self.game.enemy.boxes:
                if self.collidingWith(b.rectangle):
                    self.hit(b)
                    if self.health<=0:
                        self.health=0
                        self.dead=True
    
    def hit(self, box):
        self.health-=box.damage
        box.remove()

    def draw(self, screen):
        if not self.dead:
            rect=self.rectangle
            if self.colliding:
                color=YELLOW
            else:
                color=PURPLE
            # pygame.draw.rect(screen, color, rect)
            screen.blit(self.image, (rect.x, rect.y))

class Enemy:
    boxes=[]
    def __init__(self,x,y,size, image, game):
        self.game=game
        self.x=x
        self.y=y
        self.size=size
        self.frequency=36
        self.waitTime=self.frequency
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image, (self.size, self.size))
       

    def attack(self):
        for b in self.boxes:
            b.go()

        if self.waitTime>0:
            self.waitTime-=1
            return
        else:
            self.waitTime=self.frequency
        
    
        num=random.randint(1,4)
        speed=random.randint(2,4)*2
        self.boxes.append(Box(num, self.boxes, speed, self.game))
        num=random.randint(1,4)
        speed=random.randint(2,4)*2
        self.boxes.append(Box(num, self.boxes, speed, self.game))
        
           
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

        for b in self.boxes:
            b.draw(screen)        

class Box:
    def __init__(self, direction, boxList, speed, game,):
        box=game.player_box
        self.boxList=boxList
        self.direction=direction
        if direction==1:
            self.spawn_top()
            self.x=random.randint(box.x-50, box.x+box.width)
        elif direction==2:
            self.spawn_right()
            self.y=random.randint(box.y-50, box.y+box.height)
        elif direction==3:
            self.spawn_bottom()
            self.x=random.randint(box.x-50, box.x+box.width)
        elif direction==4:
            self.spawn_left()
            self.y=random.randint(box.y-50, box.y+box.height)

        self.damage=5
        self.speed=speed

        self.rectangle=pygame.Rect(self.x, self.y, 50, 50)

    def spawn_top(self):
        self.y=-50
    def spawn_right(self):
        self.x=1050
    def spawn_bottom(self):
        self.y=850
    def spawn_left(self):
        self.x=-50
    
    
    def go_down(self):
        self.rectangle.y+=self.speed
    def go_left(self):
        self.rectangle.x-=self.speed
    def go_up(self):
        self.rectangle.y-=self.speed
    def go_right(self):
        self.rectangle.x+=self.speed

    def go(self):
        if self.direction==1:
            self.go_down()
        elif self.direction==2:
            self.go_left()
        elif self.direction==3:
            self.go_up()
        elif self.direction==4:
            self.go_right()

        if self.rectangle.x<-100 or self.rectangle.x>WIDTH+100 or self.rectangle.y<-100 or self.rectangle.y>HEIGHT+100:
            self.remove()

    def remove(self):
        self.boxList.remove(self)
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rectangle)

class Screen:
    def draw():
        pass
    def update():
        pass

class Game(Screen):
    def __init__(self):
        self.ticks=0
        self.seconds=0
        self.minutes=0
        self.allThings=[]
        self.player_box=pygame.Rect(WIDTH/2-350/2, 300, 350, 350)
        self.player1= Player(pygame.Rect(500,500,25,25), "assets/purpleSOUL.png", 4, self)
        self.player2= Player(pygame.Rect(500,500,25,25), "assets/yellowSOUL.png", 4, self)
        self.enemy = Enemy(WIDTH/2-100,50,200,"assets/EnemyBox4.png", self)

    

    def draw_box(self, screen):
        box=self.player_box
        point=4
        pygame.draw.line(screen, WHITE, (box.x, box.y), (box.x+box.width, box.y), point)
        pygame.draw.line(screen, WHITE, (box.x+box.width, box.y), (box.x+box.width, box.y+box.height), point)
        pygame.draw.line(screen, WHITE, (box.x+box.width, box.y+box.height), (box.x, box.y+box.height), point)
        pygame.draw.line(screen, WHITE, (box.x, box.y+box.height), (box.x, box.y), point)

    def draw_health(self, screen, p1, p2):
        pygame.draw.rect(screen, RED, (20,10,50,20))
        if not p1.dead:
            pygame.draw.rect(screen, GREEN, (20,10,p1.health,20))
            screen.blit(p1.image, (30, 35))

        pygame.draw.rect(screen, RED, (930,10,50,20))
        if not p2.dead:
            pygame.draw.rect(screen, GREEN, (930,10,p2.health,20))
            screen.blit(p2.image, (940, 35))
        
    def draw(self, screen):
        self.player1.draw(screen)
        self.player2.draw(screen)
        self.enemy.draw(screen)
    
        self.draw_box(screen)
        self.draw_health(screen, self.player1, self.player2)

    def update(self):
        self.player1.move2()
        self.player2.move()
        self.enemy.attack()
        self.goTime()

    def switch_screens(self):
        if self.player1.dead and self.player2.dead:
            return TryAgain(self)
        else:
            return self
        
    def goTime(self):
        if not (self.player1.dead and self.player2.dead):
            self.ticks+=1
            if self.ticks>=60:
                self.ticks=0
                self.seconds+=1
            if self.seconds>=60:
                self.seconds=0
                self.minutes+=1
    
class TryAgain(Screen):
    def __init__(self, gameScreen1):
        self.gameScreen=gameScreen1
        self.text = font.render('Final Time: ', True, WHITE)
        self.text2 = font.render('Try Again? [PRESS SPACE]', True, WHITE)

    def draw(self, screen):
        screen.blit(self.text, (200,200))
        screen.blit(self.text2, (200,400))
    
    def update(self):
        self.text = font.render('Final Time: '+str(self.gameScreen.minutes)+' Minutes, '+str(self.gameScreen.seconds)+' seconds', True, WHITE)
    
    def switch_screens(self):
        keys_down=pygame.key.get_pressed()

        if keys_down[pygame.K_SPACE]:
            return Game()
        else:
            return self
        
    
        

gameScreen = Game()
activeScreen = gameScreen
n=0 







while running:
    n+=1
    print(n)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE
    activeScreen.update()
    activeScreen=activeScreen.switch_screens()
    
    # DRAW
    screen.fill(BLACK)

    activeScreen.draw(screen)

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()