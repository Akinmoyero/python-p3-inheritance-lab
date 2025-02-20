import pytest
from lib.user import User  # Explicitly import User
from lib.teacher import Teacher  # Import Teacher

class TestTeacher:
    def test_is_subclass(self):
        '''is a subclass of "User".'''
        assert User in Teacher.__bases__

    def test_initializes_with_name(self):
        '''initializes with first and last name.'''
        teacher = Teacher("Jane", "Smith")
        assert teacher.first_name == "Jane"
        assert teacher.last_name == "Smith"

    def test_has_knowledge_list(self):
        '''has an attribute called "knowledge", a list with len > 0.'''
        assert isinstance(Teacher.knowledge, list)
        assert len(Teacher.knowledge) > 0

    def test_teach_method(self):
        '''teaches from list of knowledge.'''
        teacher = Teacher("Jane", "Smith")
        assert teacher.teach() in Teacher.knowledge
