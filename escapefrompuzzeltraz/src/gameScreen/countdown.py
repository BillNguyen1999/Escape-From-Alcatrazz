import os
import pygame
from pygame.sprite import Sprite, Group
 
class Text(Sprite):
    def __init__(self, text, font, color, position, anchor="topleft"):
        Sprite.__init__(self)
        self._text = text
        self._font = font
        self._color = color
        self._anchor = anchor
        self._position = position
        self.render()
 
    def render(self):
        self.image = self._font.render(self._text, 1, self._color)
        self.rect = self.image.get_rect(**{self._anchor: self._position})
 
    def set_text(self, text):
        self._text = text
        self.render()
 
class Timer:
    def __init__(self, start, interval, callback):
        self.tick = start
        self.interval = interval
        self.callback = callback
 
    def update(self, ticks):
        while ticks > self.tick:
            self.tick += self.interval
            self.callback(self)
 
class CountDownTimer:
    def __init__(self, count, callback, interval=1000):
        self.count = count
        self.callback = callback
        self.timer = Timer(pygame.time.get_ticks(), interval, self.countdown)
 
    def countdown(self, timer):
        self.count -= 1
        self.callback(self)

    def update(self, ticks):
        if self.count >= 0:
            self.timer.update(ticks)
 
class DisplayCountDown:
    def __init__(self, count, font, color, position, anchor="topleft", interval=1000):
        self.count = count
        self.countdown = CountDownTimer(count, self.update_text, interval)
        self.display = "{:02d}"
        self.text = Text(self.display.format(self.countdown.count), font, color, position, anchor)
 
    def update_text(self, countdown):
        if countdown.count >= 0:
            self.text.set_text(self.display.format(countdown.count))
        else:
            self.text.kill()
            from gameScreen import gameLossView
 
    def update(self, ticks):
        self.countdown.update(ticks)
    
    def current_time(self):
        return self.countdown.count