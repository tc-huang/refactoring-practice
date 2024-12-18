from data_class.student import Student

class StudentHelper:
    @staticmethod
    def get_full_name(student: Student) -> str:
        return student.first_name + " " + student.last_name