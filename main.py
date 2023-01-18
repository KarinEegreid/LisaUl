# Karl Paju IS22

import pygame

pygame.init()

# Ekraani seaded
suurus = (1000, 800)
screen = pygame.display.set_mode(suurus)
pygame.display.set_caption("Karl Paju IS22 Lisa ül")
screen.fill([0, 0, 0])

# Lisame tausta
bg = pygame.image.load("happy-boy-and-girl-birthday-cake-on-table-vector-24648349.jpg")
screen.blit(bg, [0, 0])
# Logo lisamine
logo = pygame.image.load("VIKK logo.png")
logo = pygame.transform.scale(logo, [230, 75])
screen.blit(logo, [10, 40])

# Mööga lisamine
mook = pygame.image.load("Mõõk.png")
mook = pygame.transform.scale(mook, [250, 125])
screen.blit(mook, [350, 125])


# Teksti lisamine
font = pygame.font.Font(None, 100)
text = "TULEVIK 2050"

# Render text and get its rect
text = font.render(text, True, (0, 0, 0))
text_rect = text.get_rect()

# Center the rect
text_rect.center = (suurus[0] / 2, suurus[1] / 2)

# Create a new surface for the curved text
curved_text = pygame.Surface((text_rect.width, text_rect.height), pygame.SRCALPHA)

# Draw the text on the new surface
curved_text.blit(text, (0, 0))

# Draw the curved text on the screen
pygame.draw.arc(curved_text, (0, 0, 0), text_rect, 0, 3.14, 1)
screen.blit(curved_text, text_rect)

pygame.display.flip()

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
