def format_message(template, **kwargs):
    return template.format(**kwargs)

print(format_message('hello, {name}', name='jack'))