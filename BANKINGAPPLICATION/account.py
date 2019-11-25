# coding=utf-8

from user import User


class Account(User):
    """
    Operations that are done on a User's account
    """
    def __init__(self, account_no, date_of_opening, account_type, f_name,
                 l_name, age, gender, m_number):
        """
        Adding account details when the user creates an account
        """
        super().__init__(f_name, l_name, age, gender, m_number)
        self.account_no = account_no
        self.date_of_opening = date_of_opening
        self.account_type = account_type
        self.bank_name = 'union bank of india'
        self.ifsc_code = 'UBIN0534455'

    def show_account_info(self):
        """
        Return neatly formatted account information of the user
        """
        print(f'*** {self.bank_name.upper()} ***')
        print(f'IFSC: {self.ifsc_code}')
        print(f'Account No: {self.account_no}')
        print(f'Account Type: {self.account_type.title()}')
        self.user.show_user_info()
        print(f'Date Of Opening: {self.date_of_opening}')
