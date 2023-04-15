#!/usr/bin/env python3
from brain_games import cli
from brain_games import calc
from brain_games import even
from brain_games import gcd
from brain_games import progression
from brain_games import prime


def welcome_user():
    cli.welcome_user()


def calc_game():
    calc.calc_game()


def even_game():
    even.even_game()


def gcd_game():
    gcd.gcd_game()


def progression_game():
    progression.progression_game()


def prime_game():
    prime.prime_game()


if __name__ == '__main__':
    welcome_user()
    calc_game()
    even_game()
    gcd_game()
    progression_game()
    prime.prime_game()
