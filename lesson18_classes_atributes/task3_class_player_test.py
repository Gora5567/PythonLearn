from task3_class_player import Player


def test_add_score():
    p = Player()

    result = p.add_score()

    assert result == 1
