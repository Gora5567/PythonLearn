from task5_merge_with_defaults import merge_with_defaults

def test_merge_with_defaults():
    what_to_do = {"greetings": "hello", "gender": "male"}
    assert(merge_with_defaults(what_to_do, name="jack", car="bmw")) == {"greetings": "hello", "gender": "male", "name": "jack", "car": "bmw"}
    