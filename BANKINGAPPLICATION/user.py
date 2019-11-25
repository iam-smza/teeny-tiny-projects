# coding=utf-8


class User:
    """
    A simple attempt to represent a User
    """
    def __init__(self, f_name, l_name, age, gender, m_number):
        """
        Initialize the details of the User
        """
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
        self.m_number = m_number

    def get_user_name(self):
        """
        Prints a neatly formatted name of the User
        """
        full_name = f'{self.f_name} {self.l_name}'
        return full_name

    def show_user_info(self):
        """
        Prints a neatly formatted information of the User
        """
        name = self.get_user_name()
        print(f'Name: {name.title()}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender.title()}')
        print(f'Mobile: {self.m_number}')
