import pygame
import time


class Sound:
    def __init__(self, file):
        pygame.init()
        pygame.mixer_music.load(file)
        self.isPlaying = False

    def play(self):
        if not self.isPlaying:
            self.isPlaying = True
            pygame.mixer_music.play(-1)

    def stop(self):
        self.isPlaying = False
        pygame.mixer_music.fadeout(1000)
