#!/usr/bin/env python3
from brain_games.game_engine import start_game
from brain_games import cli
from brain_games.games import prime
from brain_games.games import calc
from brain_games.games import even
from brain_games.games import gcd
from brain_games.games import progression


def welcome_user():
    cli.welcome_user()


def game_prime():
    start_game(prime)


def game_calc():
    start_game(calc)


def game_even():
    start_game(even)


def game_gcd():
    start_game(gcd)


def game_progression():
    start_game(progression)


if __name__ == '__main__':
    welcome_user()
    game_prime()
    game_calc()
    game_even()
    game_gcd()
    game_progression()
