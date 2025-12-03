from task7_class_counter import Counter

def test_total_created_increases():
    start = Counter.total_created

    c1 = Counter()
    c2 = Counter()
    c3 = Counter()

    assert Counter.total_created == start + 3


def test_separate_instances_do_not_have_own_total():
    c1 = Counter()
    c2 = Counter()

    # у объектов нет собственного total_created
    assert not hasattr(c1, "total_created")
    assert not hasattr(c2, "total_created")
    # но класс имеет
    assert hasattr(Counter, "total_created")
