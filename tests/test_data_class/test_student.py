from data_class.student import Student
from data_class.helper import StudentHelper

def test_get_full_name():
    student = Student("John", "Doe")
    assert student.get_full_name() == "John Doe"