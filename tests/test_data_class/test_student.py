from data_class.student import Student

def test_get_full_name():
    student = Student("John", "Doe")
    assert student.get_full_name() == "John Doe"