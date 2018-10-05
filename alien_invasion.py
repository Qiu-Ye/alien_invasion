import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	play_button = Button(ai_settings, screen, "Play")

	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	gf.create_fleet(ai_settings, screen, ship, aliens)

	while True:
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, ship, aliens, bullets, sb)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)
		
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb)

run_game()


