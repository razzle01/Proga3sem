# test.py
import unittest
from main import Group, Student, ManyToMany


class TestGroup(unittest.TestCase):
    def test_add_student(self):
        group = Group(1, "TestGroup")
        student = Student(1, "TestStudent", 2000, group)

        group.add_student(student)
        self.assertIn(student, group.students)


class TestStudent(unittest.TestCase):
    def test_student_str(self):
        group = Group(1, "TestGroup")
        student = Student(1, "TestStudent", 2000, group)
        self.assertEqual(str(student), "TestStudent (2000)")


class TestManyToMany(unittest.TestCase):
    def test_many_to_many_creation(self):
        many_to_many = ManyToMany(1, 2)
        self.assertEqual(many_to_many.student_id, 1)
        self.assertEqual(many_to_many.group_id, 2)


if __name__ == '__main__':
    unittest.main()
