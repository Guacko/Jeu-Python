#============================================ IMPORTATION =======================================================
if True:#importation modules
    import pygame
    import random
    pygame.init()
if True:# réglage fenêtre
    screenWidth = 1200                                          # Largeur Fenêtre
    screenHeight = 600                                          # Hauteur de la Fenêtre
    displaySurface = pygame.display.set_mode((screenWidth,screenHeight))   # Taille de la Fenêtre
    pygame.display.set_caption("Jeu Python")                    # Titre de la Fenêtre
    clock = pygame.time.Clock()
if True:# Importation des Sprites
    spriteBackgrounds = [pygame.image.load('Sprites/Background/GameOver/GameOver.jpg'),pygame.image.load('Sprites/Background/_PNG/4/background.png'),pygame.image.load('Sprites/Background/PauseMenu/pausemenuabg.png')]
    spritePlayerRight = [pygame.image.load('Sprites/Characters/player/R1.png'), pygame.image.load('Sprites/Characters/player/R2.png'), pygame.image.load('Sprites/Characters/player/R3.png'), pygame.image.load('Sprites/Characters/player/R4.png'), pygame.image.load('Sprites/Characters/player/R5.png'), pygame.image.load('Sprites/Characters/player/R6.png'), pygame.image.load('Sprites/Characters/player/R7.png'), pygame.image.load('Sprites/Characters/player/R8.png'), pygame.image.load('Sprites/Characters/player/R9.png')]
    spritePlayerLeft = [pygame.image.load('Sprites/Characters/player/L1.png'), pygame.image.load('Sprites/Characters/player/L2.png'), pygame.image.load('Sprites/Characters/player/L3.png'), pygame.image.load('Sprites/Characters/player/L4.png'), pygame.image.load('Sprites/Characters/player/L5.png'), pygame.image.load('Sprites/Characters/player/L6.png'), pygame.image.load('Sprites/Characters/player/L7.png'), pygame.image.load('Sprites/Characters/player/L8.png'), pygame.image.load('Sprites/Characters/player/L9.png')]
    spritePlayerDefault = pygame.image.load('Sprites/Characters/player/standing.png')
    spriteEnemy1Right = [pygame.image.load('Sprites/Characters/Troll/R1E.png'), pygame.image.load('Sprites/Characters/Troll/R2E.png'), pygame.image.load('Sprites/Characters/Troll/R3E.png'), pygame.image.load('Sprites/Characters/Troll/R4E.png'), pygame.image.load('Sprites/Characters/Troll/R5E.png'), pygame.image.load('Sprites/Characters/Troll/R6E.png'), pygame.image.load('Sprites/Characters/Troll/R7E.png'), pygame.image.load('Sprites/Characters/Troll/R8E.png'), pygame.image.load('Sprites/Characters/Troll/R9E.png')]
    spriteEnemy1Left = [pygame.image.load('Sprites/Characters/Troll/L1E.png'), pygame.image.load('Sprites/Characters/Troll/L2E.png'), pygame.image.load('Sprites/Characters/Troll/L3E.png'), pygame.image.load('Sprites/Characters/Troll/L4E.png'), pygame.image.load('Sprites/Characters/Troll/L5E.png'), pygame.image.load('Sprites/Characters/Troll/L6E.png'), pygame.image.load('Sprites/Characters/Troll/L7E.png'), pygame.image.load('Sprites/Characters/Troll/L8E.png'), pygame.image.load('Sprites/Characters/Troll/L9E.png')]
    spriteBackgrounds[2] = pygame.transform.scale(spriteBackgrounds[2],(1000,600))

#============================================= VARIABLES ========================================================
if True:#variables
    if True:# Paramètre programme
        run = True
        fps = 27
        spaceHold = False
        firstStage = 0
        gameOver = False
        pause = False
                                 # Réglage images/secondes        
    if True:# Barre de vies
        lifeBarHeightOffset = 15
        defaultLifeBarWidth = 60
        defaultLifeBarEight = 3
    if True:# Personnages
        if True:# Commun
            xdefault = screenWidth/2
            ydefault = 480
            punch = 4
            defaultLife = 100
            minimumDistanceBetweenCharacters = 40
            weaponReadyDelayPlayer = 50
        if True:# Enemi
            enemyLifeStage=[10,15,30,50,100,200,500,1000,5000,10000]
            enemyWeaponStage=[4,4,6,8,10,15,30,25,50,100]
    if True:# Couleurs
        red = [255,0,0]
        green = [0,255,0]
        blue = [0,0,255]
        white = [255,255,255]
        black = [0,0,0]
    if True:# Bouttons
        defaultButtonWidth = 370
        defaultButtonHeight = 50
        defaultButtonX = (screenWidth/2)-(defaultButtonWidth/2)
        defaultButtonY = (screenHeight/6.5)
    if True:# Texte
        textHeigt = 32
        textOffsetHorizontal = 95
        font = pygame.font.Font('freesansbold.ttf',textHeigt) 
        textResumeButton = font.render('Reprendre',True,black)
        textRestartButton = font.render('Recommencer',True,black)
        textQuitButton = font.render('Quitter',True,black) 
#============================================== CLASSES =========================================================
if True:# Classes
    class player(object):# Le Joueur
        def __init__(self,x,y,width,height,life):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.speed = 5
            self.speedWalk = 5
            self.speedSprint = 10
            self.isJump = False
            self.left = False
            self.right = False
            self.walkCount = 0
            self.jumpCount = 10
            self.jumpPower = 0.2
            self.jumpSpeed = 2
            self.weapon = punch
            self.life = life
            self.weaponReady = True
            self.weaponReadyCounter = 0
        def draw(self, displaySurface):# Affichage/Animation personnage
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if self.left:
                displaySurface.blit(spritePlayerLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                displaySurface.blit(spritePlayerRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
            else:
                displaySurface.blit(spritePlayerDefault, (self.x,self.y))
    class enemy(object):# Un enemi
        def __init__(self,x,y,width,height,life):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.speed = 3
            self.left = False
            self.walkCount = 0
            self.weapon = enemyWeaponStage[0]
            self.life = enemyLifeStage[0]
            self.inRange = False
            self.totalLife=self.life
        def draw(self, displaySurface):# Affichage/Animation personnage
            if self.inRange:
                if self.walkCount >= 27:
                    self.walkCount = 15
            else:
                if self.walkCount + 1 >= 18:
                    self.walkCount = 0
            if self.left:
                displaySurface.blit(spriteEnemy1Left[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:
                displaySurface.blit(spriteEnemy1Right[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
    class lifeBar(object):# Une barre de vie
        def __init__(self,total,current,x,y,width,height):
            self.total = total
            self.current = current
            self.x = x
            self.y = y
            self.width = width
            self.height = height
        def drawBarLife(self):
            pygame.draw.rect(displaySurface,black,(self.x,self.y,self.width,self.height))
            if self.current>=0:
                pygame.draw.rect(displaySurface,red,(self.x,self.y,((self.width/self.total)*self.current),self.height))
    class stage(object):# Etape du jeu
        def __init__(self,stage):
            self.currentStage=0
            self.oldStage=0
    class button(object):# Bouttons
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
        def drawButton(self):
            pygame.draw.rect(displaySurface,white,(self.x,self.y,self.width,self.height))
            pygame.draw.rect(displaySurface,black,(self.x,self.y,self.width,self.height),4)
if True:# Création des Objets
    if True:# niveaux
        stage = stage(firstStage)
    if True:# joueur
        player = player(xdefault,(ydefault-32),64,64,defaultLife)
    if True:# enemis
        enemy = enemy(10,(ydefault-32),64,64,defaultLife)
    if True:# barre de vies
        playerLifeBar = lifeBar(defaultLife,defaultLife,player.x,(player.y-lifeBarHeightOffset),defaultLifeBarWidth,defaultLifeBarEight)
        enemyLifeBar = lifeBar(defaultLife,defaultLife,player.x,(player.y-lifeBarHeightOffset),defaultLifeBarWidth,defaultLifeBarEight)
    if True:# Bouttons
        resumeButton = button(defaultButtonX,defaultButtonY*2,defaultButtonWidth,defaultButtonHeight)
        restartButton = button(defaultButtonX,defaultButtonY*3,defaultButtonWidth,defaultButtonHeight)
        quitButton = button(defaultButtonX,defaultButtonY*4,defaultButtonWidth,defaultButtonHeight)

#============================================= FONCTIONS ========================================================
def redrawGameWindow():# Rafraichissement de l'écran
    if not(pause):# Jeu
        displaySurface.blit(spriteBackgrounds[1],(0,-100))

        # Life Bars
        playerLifeBar.drawBarLife()
        enemyLifeBar.drawBarLife()

        #characters
        enemy.draw(displaySurface)
        player.draw(displaySurface)

        if gameOver:
            displaySurface.blit(spriteBackgrounds[0],(-37,-100))
    else:# Menu Pause
        displaySurface.blit(spriteBackgrounds[2],((screenWidth/2)-495,(screenHeight/2)-320))

        # Bouttons menu  
        resumeButton.drawButton()
        restartButton.drawButton() 
        quitButton.drawButton()

        # texte bouttons
        displaySurface.blit(textResumeButton,(((resumeButton.x+(resumeButton.width/2))-textOffsetHorizontal),(resumeButton.y+resumeButton.height/2)-textHeigt/2))
        displaySurface.blit(textRestartButton,(((restartButton.x+(restartButton.width/2))-textOffsetHorizontal),(restartButton.y+restartButton.height/2)-textHeigt/2))
        displaySurface.blit(textQuitButton,(((quitButton.x+(quitButton.width/2))-textOffsetHorizontal),(quitButton.y+quitButton.height/2)-textHeigt/2))


    # Display update
    pygame.display.update()

#============================================ BOUCLE INFINIE ====================================================
while run:
    redrawGameWindow()# Redessine les nouveaux paramètres à l'écran
    if True:# Système
            clock.tick(fps)
            for event in pygame.event.get(): # Détection d'évenements
                 if event.type == pygame.QUIT: # Croix rouge d'étectée = quitter
                    run = False
            keys = pygame.key.get_pressed() # keys prend les touches pressées du clavier
            if keys[pygame.K_F11]: # [F11] plein écran
                pygame.display.toggle_fullscreen

            if keys[pygame.K_F4] and keys[pygame.K_LALT]:# [Alt] + [F4] pour fermer
                run=False 
    if keys[pygame.K_ESCAPE]:#Menu Pause
        if not(pHold):
            pause = not(pause)
            pHold = True
    else:
        pHold = False
    if not(pause):# si le jeu n'est pas en pause
        if True:# Actions automatiques
            if True:# Joueur
                if player.life<=0:
                    gameOver=True
            if True:# Enemi
                if ((player.x-enemy.x)>minimumDistanceBetweenCharacters)|((enemy.x-player.x)>minimumDistanceBetweenCharacters):# Enemi va aller à coté du joueur
                    enemy.inRange = False
                    if player.x>enemy.x:
                        enemy.x += enemy.speed
                        enemy.left = False
                    else:
                        enemy.x -= enemy.speed
                        enemy.left = True
                else:
                    enemy.inRange = True
                if enemy.life<=0:
                    stage.currentStage += 1
            if True:# Niveaux
                if not(stage.currentStage==stage.oldStage):
                    enemy.x=random.randrange(0,screenWidth)
                    enemy.y=ydefault-32
                    enemy.life=enemyLifeStage[stage.currentStage]
                    enemy.totalLife=enemy.life
                    stage.oldStage=stage.currentStage        
            if True:# Life bar update position / current life
                playerLifeBar.x = player.x
                playerLifeBar.y = (player.y-lifeBarHeightOffset)
                playerLifeBar.current=player.life
                if enemy.walkCount>26:
                    player.life -= enemy.weapon

                enemyLifeBar.x = enemy.x
                enemyLifeBar.y = (enemy.y-lifeBarHeightOffset)
                enemyLifeBar.current = enemy.life
                enemyLifeBar.total=enemy.totalLife
        if True:# Actions des touches      
            if True:# Actions sur "Player"
            
                if keys[pygame.K_a] and player.x > (screenWidth-screenWidth):# [A] Gauche
                        player.x -= player.speed
                        player.left = True
                        player.right = False
                
                elif keys[pygame.K_d] and player.x < screenWidth - player.width - player.speed:# [D] Droite
                    player.x += player.speed
                    player.right = True
                    player.left = False      
                
                elif keys[pygame.K_s]:# [S] Bas(face)
                    player.right = False
                    player.left = False
                    walkCount = 0
                else:
                    player.walkCount = 0

                if keys[pygame.K_LSHIFT]:# [L_SHIFT] Sprint
                    player.speed = player.speedSprint
                else:
                    player.speed = player.speedWalk
                
                if not(player.isJump):# [W] Saute
                    if keys[pygame.K_w]:
                        player.isJump = True
                        player.right = False
                        player.left = False
                        player.walkCount = 0
                else:
                    if player.jumpCount >= -10:
                        neg = 1
                        if player.jumpCount < 0:
                            neg = -1
                        player.y -= (player.jumpCount ** 2) * player.jumpPower * neg
                        player.jumpCount -= player.jumpSpeed
                    else:
                        player.isJump = False
                        player.jumpCount = 10

                if keys[pygame.K_SPACE] :# [ESPACE] attaque
                    if ((player.x <= (enemy.x + minimumDistanceBetweenCharacters) and player.x >= (enemy.x-minimumDistanceBetweenCharacters)) and (player.y <= (enemy.y+minimumDistanceBetweenCharacters) or player.y>(enemy.y-minimumDistanceBetweenCharacters)) and not(spaceHold)):
                        enemy.life -= player.weapon
                        spaceHold = True
                else:
                    spaceHold = False            
    else:# Menu Pause

        # -------- Boutons ----------------
        xMouse,yMouse = pygame.mouse.get_pos()
        button1Mouse,button2Mouse,button3Mouse = pygame.mouse.get_pressed()

        # Boutton Reprendre
        if (button1Mouse and ((resumeButton.x + resumeButton.width) > xMouse > resumeButton.x)) and ((resumeButton.y + resumeButton.height) > yMouse > resumeButton.y):
            pause=False
        
        # Boutton Recommancer
        if (button1Mouse and ((restartButton.x + restartButton.width) > xMouse > restartButton.x)) and ((restartButton.y + restartButton.height) > yMouse > restartButton.y):
            player.life=defaultLife
            stage.currentStage=0
            enemy.x = random.randrange(0,screenWidth)
            enemy.life=enemyLifeStage[0]
            pause=False

        # Boutton quitter
        if (button1Mouse and ((quitButton.x + quitButton.width) > xMouse > quitButton.x)) and ((quitButton.y + quitButton.height) > yMouse > quitButton.y):
            run=False

#======================================== FIN DE LA BOUCLE INFINIE ==============================================
pygame.quit()# le jeu quitte