# coding=utf-8


class Manager:
    """
    Contains various Authoritive operations to help handling the environment
    """
    def __init__(self):
        """
        Initialize data structures for carrying out Accounts and User handling
        functions
        """
        self.user_info = list()
        self.existing_users = list()
        self.user_data = dict()

    def show_total_user_count(self):
        """
        Returns the count of existing users
        """
        user_count = len(self.existing_users)
        print(f'Total User Count: {user_count}')

    def show_active_user_count(self):
        """
        Shows the number of active users
        In this case: Users who have transacted within the period of 365 days
        """
        pass

    def show_banned_users(self):
        """
        Show blacklisted users count and names
        """
        pass

    def show_dormant_user_count(self):
        """
        Shows the number of dormant accounts
        In this case: Users who have not transacted within the period
        of 365 days
        """
        pass
