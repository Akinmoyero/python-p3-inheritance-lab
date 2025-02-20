import pytest
from lib.user import User  # Explicitly import User
from lib.student import Student  # Import Student

class TestStudent:
    def test_is_subclass(self):
        '''is a subclass of "User".'''
        assert User in Student.__bases__

    def test_initializes_with_name(self):
        '''initializes with first and last name.'''
        student = Student("John", "Doe")
        assert student.first_name == "John"
        assert student.last_name == "Doe"

    def test_has_empty_knowledge_list(self):
        '''initializes with empty list attribute "knowledge".'''
        student = Student("John", "Doe")
        assert isinstance(student.knowledge, list)
        assert len(student.knowledge) == 0

    def test_learn_method(self):
        '''learns from a string and adds to self.knowledge.'''
        student = Student("John", "Doe")
        student.learn("Python is fun!")
        assert "Python is fun!" in student.knowledge
