import pygame, random, pendulum
from random import randint
pygame.init()
infoObject = pygame.display.Info()

##########################################
# Jeu du Snake avec de nouvelles rêgles : IMPOSSIBLE DE MOURIR et accélération du jeu après avoir mangé
##########################################

# Toutes les couleurs
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
tabColor = [white, yellow, red, green, blue]

# Résolution de l'écran
dis_width = round(infoObject.current_w/10)*10
dis_height = round(infoObject.current_h/10)*10

# Ou de la fenêtre
dis_width = 600
dis_height = 400

# Initialisation de la fenêtre
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Serpent par Dorian & Tom')

# Initialisation du temps
clock = pygame.time.Clock()

# Initialisation du serpent
snake_block = 10#pixel
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

# Affichage du score
score_font = pygame.font.SysFont("arial", 35)
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Affichage du temps
time_font = pygame.font.SysFont("arial", 35)
def Your_time(time):
    value = score_font.render("Time: " + time, True, yellow)
    dis.blit(value, [dis_width/1.5, 0])
    
def gameLoop():
    start = pendulum.now()
    tabTime = []
    game_over = False
    snake_speed = 15
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    # Positionnement de la première pomme
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    # Actualisation de la fenêtre à chaque tick du jeu
    while not game_over:

        # Déplacement du serpent avec les touches du clavier
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                if event.key == pygame.K_LEFT:
                    y1_change = 0
                    x1_change = -snake_block
                elif event.key == pygame.K_RIGHT:
                    y1_change = 0
                    x1_change = snake_block
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Si le serpent sort de l'écran il revient à l'opposé
        if x1 >= dis_width:
            x1 = 0;
        elif x1 <= 0:
            x1 = dis_width;
        elif y1 >= dis_height:
            y1 = 0;
        elif y1 <= 0:
            y1 = dis_height;

        # Il bouge à chaque tick
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, tabColor[randint(0, len(tabColor)-1)], [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        our_snake(snake_block, snake_List)
        time_game = str(pendulum.now().diff(start).in_seconds());

        # Actualisation des textes
        Your_score(Length_of_snake - 1)
        Your_time(time_game)
 
        pygame.display.update()
 
        # Si le serpent mange une pomme
        time = pendulum.now()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1 #Le serpent grandit
            snake_speed += 20 #J'accélère le jeu
            tabTime.append(int(pendulum.now().diff(time).in_seconds())) #J'enregistre le temps à chaque fois
            moyenne = sum(tabTime)/len(tabTime)
            time = pendulum.now();
        clock.tick(snake_speed)
    
    # Messsage affiché à la fin de la partie
    print(f"Votre moyenne est de {round(moyenne)}s par obtention de pomme !")
    print(f"La partie a duré {time_game}s !")

gameLoop()

##########################################
########### PETIT CODE MARRANT ###########
##########################################

# import io, pendulum, time, qrcode, requests, json
# from MyQR import myqr as mq

# api = 'c76f924afd0743b7b5d225211211708'
# ville = 'Toulouse'
# response = requests.request("GET", f"http://api.weatherapi.com/v1/current.json?key={api}&q={ville}&aqi=no")
# data = response.json()
# date = pendulum.now().format('DD MMM YYYY HH:mm:ss')
# text = f"{date} à {data['location']['name']}, il fait {int(data['current']['temp_c'])}° et le temps est {data['current']['condition']['text']}"

# # print(json.dumps(response.json(), sort_keys=True, indent=4))


# # while True:
# #     qr = qrcode.QRCode()
# #     qr.add_data(text)
# #     f = io.StringIO()
# #     qr.print_ascii(out=f)
# #     f.seek(0)
# #     print(f.read())
# #     time.sleep(1)


# mq.run(text, save_name = './tco_qr.png')
