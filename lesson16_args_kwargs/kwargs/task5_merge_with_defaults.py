def merge_with_defaults(defaults, **kwargs):
    if type(defaults) is not dict:
        return kwargs

    merged = defaults
    merged.update(kwargs)

    return merged


what_to_do = {"greetings": "hello", "gender": "male"}
result = merge_with_defaults(what_to_do, name="jack", car="bmw")
print(result)
