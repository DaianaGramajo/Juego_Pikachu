import pygame,random
pygame.init()

ancho=800
alto=600
negro=(0,0,0)
blanco=(255,255,255)
rojo=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
plomo=(232,224,224)


pantalla=pygame.display.set_mode((ancho,alto))
icono= pygame.image.load("assets/poke.png")
pygame.display.set_caption("Pokemon")
pygame.display.set_icon(icono)
reloj=pygame.time.Clock()

#fuentes
pequeñafuente=pygame.font.SysFont("comicsansms",15)
medianafuente=pygame.font.SysFont("comicsansms",30)
grandefuente=pygame.font.SysFont("comicsansms",50)
font = pygame.font.SysFont('Consolas', 30)


#datos de boton
boton1=(300,290)
tamboton=(200,45)
colorboton1=[plomo,rojo]
boton2=(300,340)
colorboton2=[plomo,rojo]
boton3=(300,390)
colorboton3=[plomo,rojo]
boton4=(450,300)
colorboton4=[plomo,rojo]
boton5=(450,400)
colorboton5=[plomo,rojo]
boton6=(200,200)
colorboton6=[plomo,rojo]
boton7=(200,300)
colorboton7=[plomo,rojo]
boton8=(300,390)
colorboton8 =[plomo,rojo]
boton9 =(450,200)
colorboton9 =[plomo,rojo]





def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("comicsansms", size)
	text_surface = font.render(text, True,negro)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (round(x), round(y))
	surface.blit(text_surface, text_rect)

def draw_shield_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = round(percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, verde, fill)
	pygame.draw.rect(surface, blanco, border, 2)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/p3.png").convert()
		self.image.set_colorkey(blanco)
		self.rect = self.image.get_rect()
		self.rect.centerx = ancho // 2
		self.rect.bottom = alto - 10
		self.speed_x = 0
#		self.shield = 100

	def update(self):
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if self.rect.right > ancho:
			self.rect.right = ancho
		if self.rect.left < 0:
			self.rect.left = 0

	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet)
		bullets.add(bullet)
		laser_sound.play()

	

class Pokebol(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(pokebol_images)
		self.image.set_colorkey(blanco)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(ancho - self.rect.width)
		self.rect.y = random.randrange(-140, -100)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-2, 2)

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > alto + 10 or self.rect.left < -40 or self.rect.right > ancho + 40:
			self.rect.x = random.randrange(ancho - self.rect.width)
			self.rect.y = random.randrange(-140, - 100)
			self.speedy = random.randrange(1, 10)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("assets/rayito1.PNG")
		self.image.set_colorkey(negro)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center 
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 # VELOCIDAD DE LA EXPLOSION

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
				self.kill()
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

pokebol_images = []
pokebol_list = ["assets/great3.png", "assets/master2.png","assets/safari1.png","assets/poke1.png","assets/ultra2.png"]
for img in pokebol_list:
	pokebol_images.append(pygame.image.load(img).convert())

####----------------EXPLOSTION IMAGENES --------------
explosion_anim = []
for i in range(9):
	file = "assets/regularExplosion0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(negro)
	img_scale = pygame.transform.scale(img, (70,70))
	explosion_anim.append(img_scale)

# Cargar imagen de fondo
background = pygame.image.load("assets/back.jpg").convert()
pausa1=pygame.image.load("assets/pausar.jpg").convert()
perdio=pygame.image.load("assets/perdio.jpg").convert()
credits=pygame.image.load("assets/cred.jpg").convert()
menu=pygame.image.load("assets/fondito.png").convert()
gano=pygame.image.load("assets/gana.png").convert()


# Cargar sonidos
laser_sound = pygame.mixer.Sound("assets/pika.ogg")
explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
pygame.mixer.music.load("assets/music1.ogg")
pygame.mixer.music.set_volume(0.1)


all_sprites = pygame.sprite.Group()
pokebol_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
	pokebol = Pokebol()
	all_sprites.add(pokebol)
	pokebol_list.add(pokebol)

#Marcador / Score
score = 0

suma = 0
#----temporizador -----
counter, text = 3, '3'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)




 #----------Puntuacion-------------

def puntos(marcador):
	mensaje=tamaño="mediano".render("Puntos:  "+ str(marcador),True,negro)
	pantalla.blit(perder,[0,0])


def textoboton(msg,color,botonx,botony,ancho,alto,tamaño="pequeño"):
	textosuperficie,textorect=objetotexto(msg,color,tamaño)
	textorect.center=(botonx+ round(ancho/2),botony+round(alto/2))
	pantalla.blit(textosuperficie,textorect)


def botones(texto,superficie,estado,posicionamiento,tam,identidad=None):
	cursor=pygame.mouse.get_pos()
	click =pygame.mouse.get_pressed()

	if posicionamiento[0]+tam[0] > cursor[0] > tam[0] and posicionamiento[1]+ tam[1] > cursor[1] > tam[1] and posicionamiento[1] +tam[1] < cursor[1] + tam[1]:
		if click[0] ==1:
			if identidad == "comienzo":
				
				gameloop()

			
			elif identidad == "configuracion":
				opciones()
			elif identidad == "salir":
				quit()
			elif identidad == "Volver al menu":
				introduccion()
			elif identidad == "salirPerder":
				quit()
			elif identidad == "F1":
				gameloop()
			elif identidad =="F2":
				quit()
			elif identidad == "VolveralmenuOpciones":
				introduccion()
			elif identidad =="Intentarotravez":
				gameloop()

		boton = pygame.draw.rect(superficie,estado[1],(posicionamiento[0],posicionamiento[1],tam[0],tam[1]))
		textoboton(texto,negro,posicionamiento[0],posicionamiento[1],tam[0],tam[1])
	else:
		boton = pygame.draw.rect(superficie,estado[0],(posicionamiento[0],posicionamiento[1],tam[0],tam[1]))
		textoboton(texto,negro,posicionamiento[0],posicionamiento[1],tam[0],tam[1])
	return boton

def gano():
	gana=True
	while gana:

			pantalla.blit(gano,[0,0])
			mensaje("¡Ganaste!",negro,-200,tamaño="grande")
			mensaje("Tu puntuacion obtenida fue:  " + str(suma),negro,-150,tamaño="mediano")
			pygame.display.update()





def fin_juego():
	fin =True
	while fin:
		pantalla.blit(perdio,[0,0])
		mensaje("¡Perdiste! ",negro,-200,tamaño="grande")
		mensaje("Tu puntuacion obtenida fue:  " + str(suma),negro,-150,tamaño="mediano")
		botones("Salir",pantalla,colorboton5,boton5,tamboton,identidad="salirPerder")
		botones("Ir al menu",pantalla,colorboton4,boton4,tamboton,identidad="Volver al menu")
		botones("Volver a Jugar",pantalla,colorboton9,boton9,tamboton,identidad="Intentarotravez")


		
	#	mensaje("Presione: ",negro,-150,tamaño="mediano")
	#	mensaje("Para volver al menu: c ",negro,-80,tamaño="mediano")
	#	mensaje("Para salir del juego: x ",negro,-30,tamaño="mediano")
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:

					introduccion()
					fin=False

				if event.key == pygame.K_x:
					quit()
				if event.type == pygame.QUIT:
					fin=True


def objetotexto(texto,color,tamaño):
	if tamaño == "pequeño":
		textosuperficie = pequeñafuente.render(texto,True,color)
	if tamaño == "mediano":
		textosuperficie = medianafuente.render(texto,True,color)
	if tamaño == "grande":
		textosuperficie = grandefuente.render(texto,True,color)

	return textosuperficie, textosuperficie.get_rect()


def mensaje(msg,color,desplazamientoy=0,tamaño="pequeño"):
	textosuperficie, textorect= objetotexto(msg,color,tamaño)
	textorect.center = round(ancho/2), round(alto/2)+desplazamientoy
	pantalla.blit(textosuperficie,textorect)


	





def pausa():
	pausado=True
	pygame.mixer.music.pause()
	while pausado:
		reloj.tick(60)
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_F1:
                                        pygame.mixer.music.unpause()
                                        pausado=False
				if event.key==pygame.K_F2:
					quit()

		pantalla.blit(pausa1,[0,0])
		mensaje("Pausa",negro,-230,tamaño="grande")
		botones("Continuar",pantalla,colorboton6,boton6,tamboton,identidad="F1")
		botones("Salir",pantalla,colorboton7,boton7,tamboton,identidad="F2")
		

	#	draw_text(pantalla,"Presione: ",30,130,250)
	#	draw_text(pantalla," F1 para continuar",30,150,300)
	#	draw_text(pantalla," F2 para salir",30,130,350)
		pygame.display.flip()



def introduccion():

	intro=True

	pantalla.blit(menu,[0,0])
	while intro:
		pygame.mixer.music.stop()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro=False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					gameloop()

					intro=False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					opciones()
					intro=False	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x:
					intro=False		
			#pantalla.fill(negro)
			#pygame.draw.rect(pantalla,azul,(300,300,200,45))
			botones("Jugar",pantalla,colorboton1,boton1,tamboton,identidad="comienzo")
			botones("Controles",pantalla,colorboton2,boton2,tamboton,identidad="configuracion")
			botones("Salir",pantalla,colorboton3,boton3,tamboton,identidad="salir")
			mensaje("¡Pikachu debe sobrevivir!",negro,-200,tamaño="grande")
			#mensaje("presiona s para iniciar, presiona p para opciones, x para salir",azul,tamaño="pequeño")
			pygame.display.update()
			reloj.tick(60)


def opciones():

		waiting = True
        
		while waiting:
			pantalla.blit(credits,[0,0])
        
			mensaje(" CONTROLES ",negro,-220,tamaño="grande")
			mensaje(" Movimiento hacia la izquierda = Flecha izquierda ",blanco,-150,tamaño="mediano")
			mensaje(" Movimiento hacia la derecha = Flecha derecha",blanco,-100,tamaño="mediano")
			mensaje(" Disparos = space",blanco,-50,tamaño="mediano")
			mensaje(" Pausa = p",blanco,0,tamaño="mediano")  
			botones("Volver al menu",pantalla,colorboton8,boton8,tamboton,identidad="VolveralmenuOpciones")
		#	mensaje(" Presione  X para volver Atras",negro,150,tamaño="pequeño")
			pygame.display.flip()  # Print the contents to the screen
			for action in pygame.event.get():
				if action.type == pygame.KEYDOWN:
					if action.key == pygame.K_x:
						introduccion() 

def temporizador(): 
	
	global counter 
	global text

	var = True 
	while True:
    
			
        
		
			for event in pygame.event.get():
				if event.type == pygame.USEREVENT:
					counter-= 1
					text =str(counter).rjust(3)if counter >0 else "A jugar!"
					var= False	
					if counter ==0:

						break



				#if event.type == pygame.QUIT:break
					
			else:
				pantalla.blit(background,[0,0])

		#		 mensaje("El juego va a empezar en: ",negro,-200,tamaño="mediano")
				pantalla.blit(font.render(text, True, (negro)), (350,200))
	

				pygame.display.flip()
				 # reloj.tick(60)
				continue
			break


						


                                      
#--------BUCLE PRINCIPAL---------------------
def gameloop():

	
	player.shield =100
	salir=True
	score = 0
	global suma
	temporizador()




	pygame.mixer.music.play(loops=-1)


	while salir:
		reloj.tick(60)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir=False
				quit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					player.shoot()
				if event.key == pygame.K_p:	
					pausa()

			
		
			#mensaje("bucle pricipal del juego",rojo,tamaño="grande")
		

		all_sprites.update()

		# Colisiones pokebolas - rayito
		hits = pygame.sprite.groupcollide(pokebol_list, bullets, True, True)
		for hit in hits:

			score += 1
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)

			pokebol = Pokebol()
			all_sprites.add(pokebol)
			pokebol_list.add(pokebol)
			suma =suma+1



			   
			

		# Colisiones jugador - pokebolas
		hits = pygame.sprite.spritecollide(player, pokebol_list, True)

		for hit in hits:

			player.shield -= 25

			pokebol = Pokebol()
			all_sprites.add(pokebol)
			pokebol_list.add(pokebol)
			if player.shield <= 0:
				pygame.mixer.music.stop()
				fin_juego()
			
			if player.shield >0 and score == 30:
				gano()

		
		pantalla.blit(background, [0, 0])
	


		
		

		all_sprites.draw(pantalla)


		# Marcador
		draw_text(pantalla, str(score), 25, 770, 10)

		# ESCUDO.
		draw_shield_bar(pantalla, 5, 5, player.shield)


		pygame.display.flip()


introduccion()
quit()

gameloop()
