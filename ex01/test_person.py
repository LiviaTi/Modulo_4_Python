from person import Person

def test_person_initialization():
    p = Person("Alice", 30)
    assert p.name == "Alice"
    assert p.age == 30