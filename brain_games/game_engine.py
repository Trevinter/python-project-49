import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?' + " ")
    print(f'Hello, {name}')
    count = 0
    print(game.GAME_RULE)
    while count < 3:
        game_question, answer = game.get_game()
        print(f'Question: {str(game_question)}')
        question = prompt.string('Your answer:' + " ")
        if str(answer) == str(question.lower()):
            count += 1
            print('Correct!')
        else:
            print(f"'{question}' is wrong answer ;(."
                  f"Correct answer was '{answer}'.")
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
