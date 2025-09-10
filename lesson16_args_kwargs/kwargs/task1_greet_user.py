def greet_user(**kwargs):
    if 'name' in kwargs:
        return 'Hello, {}!'.format(kwargs['name'])
    else:
        return 'Hello, guest'
