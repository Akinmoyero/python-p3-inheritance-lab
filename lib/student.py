from lib.user import User  # Correct import

class Student(User):  # Ensure Student directly inherits from User
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Call User's constructor
        self.knowledge = []  # Initialize knowledge as an empty list

    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)  # Add new knowledge
