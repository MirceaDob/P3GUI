import pygame
import self as self

pygame.init()

self.mouse = ((0,0), 0, 0, 0, 0, 0, 0)
for event in pygame.event.get():
	if event.type == pygame.QUIT:
		self.running = 0
	elif event.type == pygame.MOUSEBUTTONDOWN:
		self.mouse[event.button] = 1
		self.mouse[0] = event.pos
		print("back button pressed")
	elif event.type == pygame.MOUSEBUTTONUP:
		self.mouse[event.button] = 0
		self.mouse[0] = event.pos
	elif event.type == pygame.MOUSEMOTION:
		self.mouse[0] = event.pos
	elif event.type == pygame.KEYDOWN:
		self.keys[event.key % 255] = 1
	elif event.type == pygame.KEYUP:
		self.keys[event.key % 255] = 0