# Karl Paju IS22 ÜL 2 Tekstide ja piltide lisamine

import pygame # Impordib pygame

pygame.init() # Käivitab pygame

#Ekraani seaded

Screen = pygame.display.set_mode([640,480]) # Ekraani loomine
pygame.display.set_caption("Karl Paju IS22 ÜL2") # Ekraanile nime andmine
Screen.fill([204,255,204]) # Täidab ekraani sisestatud värvi hex koodiga.

#Lisame taustapildid ning muud

# Tausta pildi lisamine
bg = pygame.image.load("taust.jpg") # Tausta lisamine
Screen.blit(bg,[0,0]) # Pildi asukoht

#Selleri lisamine ekraanile
seller = pygame.image.load("seller.png") # Selleri lisamine ekraanile
seller = pygame.transform.scale(seller, [150,300]) #Selleri laiuse ja pikkuse muutmine
Screen.blit(seller, [10,120]) # Selleri asukohta  paigaldamine

#Jutumulli lisamine ekraanile
jutumull = pygame.image.load("jutumull.png") # Jutumulli lisamine ekraanile
jutumull = pygame.transform.scale(jutumull, [200,200]) # jutumulli laiuse ja pikkuse muutmine
Screen.blit(jutumull, [150,30]) # jutumulli asukoha paigaldamine

# Teksti lisamine ekraanile
font = pygame.font.Font(pygame.font.match_font("arial"),15) # Lisab ekraanile teksti
text = font.render("Tervist, minu nimi on Karl", True, [255,255,255]) # Teksti muutuja ning värv

#Teksti kasti suurus
text_width = text.get_rect().width # muutuja
text_height = text.get_rect().height # muutuja

Screen.blit(text, [250-text_width/2,120-text_height/2]) # Ekraanil paigutatakse ära kus asub tekst

#Logo lisamine
logo = pygame.image.load("TULEVIK 2050 (1).png") # laeb sisse ekraanile logo
logo = pygame.transform.scale(logo, [220,65]) # määrab logo pikkuse ja laiuse
Screen.blit(logo, [0,1]) # määrab logo asukoha

#Koogi lisamine
kook = pygame.image.load("kook.png") # lisab ekraanile koogi
kook = pygame.transform.scale(kook, [120,70]) # Määrab koogi pikkuse ja laiuse
Screen.blit(kook, [320,230]) # Määrab koogi asukoha

# Mõõga lisamine
mook = pygame.image.load("mook.png") # Lisab ekraanile mõõga
mook = pygame.transform.scale(mook, [110,230]) # Määrab mõõga pikkuse ja laiuse
Screen.blit(mook, [525,100]) # Määrab mõõga asukoha

pygame.display.flip() # uuendab ekraani




# Loopi loomine
running = True

while running:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False
