# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
running = True

PURPLE=pygame.Color(150,30,245)
BLACK= pygame.Color(0,0,0)
GREEN= pygame.Color(0,255,0)
YELLOW= pygame.Color(255,255,0)





class Player:
    def __init__(self, rectangle, image, speed):
        allThings.append(rectangle)
        self.rectangle=rectangle
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image, (rectangle.width, rectangle.height))
        self.speed = speed
        self.color=PURPLE
        self.colliding=False

    def collidingWith(self, rect2):
        rect=self.rectangle
        if rect.x<=(rect2.x+rect2.width) and (rect.x+rect.width)>=rect2.x and rect.y<=(rect2.y+rect2.height) and (rect.y+rect.height)>=rect2.y:
            return True
            

    def move_left(self):
        self.rectangle.x-=self.speed
    def move_right(self):
        self.rectangle.x+=self.speed
    def move_up(self):
        self.rectangle.y-=self.speed
    def move_down(self):
        self.rectangle.y+=self.speed
        
    def move(self):
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
        for r in allThings:
            if r!=self.rectangle and self.collidingWith(r):
                self.colliding=True

    def move2(self):
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
        for r in allThings:
            if r!=self.rectangle and self.collidingWith(r):
                self.colliding=True

    def draw(self, screen):
        rect=self.rectangle
        if self.colliding:
            color=YELLOW
        else:
            color=PURPLE
        pygame.draw.rect(screen, color, rect)
        screen.blit(self.image, (rect.x, rect.y))


allThings = []

player1= Player(pygame.Rect(100,100,50,50), "assets/blueSOUL.png", 4)
player2= Player(pygame.Rect(400,100,50,50), "assets/redSOUL.png", 4)
test_rectangle=pygame.Rect(200,400,100,100)

allThings.append(test_rectangle)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE
    player1.move2()
    player2.move()

    
            

    # DRAW
    screen.fill(BLACK)

    pygame.draw.rect(screen, GREEN, test_rectangle)
    player1.draw(screen)
    player2.draw(screen)
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()