from data_class.student import Student
from data_class.helper import StudentHelper

def test_get_full_name():
    student = Student("John", "Doe")
    assert StudentHelper.get_full_name(student) == "John Doe"