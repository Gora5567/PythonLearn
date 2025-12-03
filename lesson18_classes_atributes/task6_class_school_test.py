from task6_class_school import Student


def test_student_school():
    s1 = Student("Миша", 7)
    s2 = Student("Маша", 8)

    # проверяем, что атрибут класса одинаков для обоих объектов
    assert s1.school == "№12"
    assert s2.school == "№12"
