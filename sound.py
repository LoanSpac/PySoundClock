import pygame


class Sound:
    def __init__(self):
        self.sound_path = "assets/sounds/"
        self.default_sound = "default.ogg"
        pygame.mixer.init()
        pygame.mixer.music.load(self.sound_path + self.default_sound)

    def play(self):
        pygame.mixer.music.play()
