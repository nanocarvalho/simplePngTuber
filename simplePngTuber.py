import pyaudio
import audioop
import pygame
import time
from sys import exit

# Pyagme
pygame.init()

display = pygame.display.set_mode((480, 480))
idle = pygame.image.load("idle.png").convert_alpha()
talk = pygame.image.load("talk.png").convert_alpha()

idle = pygame.transform.scale2x(idle)
talk = pygame.transform.scale2x(talk)

idleRect = idle.get_rect(center = (240, 240))
talkRect = talk.get_rect(center = (240, 240))

clock = pygame.time.Clock()
pygame.display.set_caption('SimplePngTuber')

# Pyaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=1024,
                )
                
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    data = stream.read(1024, exception_on_overflow = False)
    rms = audioop.rms(data, 2) # here's where I calculate the volume
    display.fill((0, 255, 0))
    
    if rms < 70:
        display.blit(idle, idleRect)
    else:
        display.blit(talk, talkRect)

            
    pygame.display.update()
    clock.tick(60)
