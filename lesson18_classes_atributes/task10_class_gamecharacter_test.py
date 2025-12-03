from game_character import GameCharacter

def test_take_damage_basic():
    hero = GameCharacter(100, 20, 5)
    hero.take_damage(15)
    assert hero.hp == 90  # 15 - 5 = 10

def test_take_damage_zero_after_kill():
    hero = GameCharacter(10, 5, 2)
    hero.take_damage(100)
    assert hero.hp == 0

def test_take_damage_no_effect_if_armor_is_high():
    hero = GameCharacter(50, 10, 100)
    hero.take_damage(20)
    assert hero.hp == 50
