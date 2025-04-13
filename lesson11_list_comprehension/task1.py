def task1(a):
    greetings = ['hello', 'hi', 'hey', 'hola']
    #with list comprehension
    second_letters = [word[1] for word in greetings]
    print("with list comprehension\n", second_letters)
    #without
    second_letters = [word[1] for word in greetings]
    print("without\n", second_letters)
