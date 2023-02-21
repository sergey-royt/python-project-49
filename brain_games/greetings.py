import prompt


def welcome_user():
    name = prompt.string(f'''Welcome to the Brain Games!
May I have your name? ''')
    print(f'''Hello, {name}!''')
    return name