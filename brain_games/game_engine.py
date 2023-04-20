import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?' + " ")
    print(f'Hello, {name}')
    count = 0
    print(game.rules)
    while count < 3:
        number, answer = game.right_answer()
        print(f'Question: {str(number)}')
        question = prompt.string('Your answer:' + " ")
        if str(answer) == str(question):
            count += 1
            print('Correct!')
        else:
            count += 4
            print(f"'{question}' is wrong answer ;(."
                  f"Correct answer was '{answer}'.")
            return print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
