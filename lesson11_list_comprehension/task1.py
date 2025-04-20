def task1(choice):
    greetings = ['hello', 'hi', 'hey', 'hola']
    if choose2 == 1:
        # with list comprehension
        second_letters = [word[1] for word in greetings]
        print("with list comprehension\n", second_letters)
    elif choose2 ==2:
        # without
        second_letters = []
        for word in greetings:
            second_letters.append(word[1])
        print(second_letters)
    else:
        print("wrong input")
