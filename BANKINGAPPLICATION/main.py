# coding=utf-8

# PROJECT NAME: Banking Application
# PROJECT VERSION: 0.0.0.7
# DATE CREATED: 11/25/2019
# DATE UPDATED: 11/26/2019
# MAINTAINER: ZAMRAN ALI
# GITHUB: https://www.github.com/iam-smza/

from os import path, remove
from random import choice, randint

from account import Account
from manager import Manager

if __name__ == "__main__":

    # instantiation of manager to store user and account information
    manager = Manager()

    names = [
        'emma', 'olivia', 'ava', 'isabella', 'sophia', 'charlotte', 'mia',
        'amelia', 'harper', 'evelyn', 'abigail', 'emily', 'elizabeth', 'mila',
        'ella', 'avery', 'sofia', 'camila', 'aria', 'scarlett', 'victoria',
        'madison', 'luna', 'grace', 'chloe', 'penelop', 'layla', 'riley',
        'zoey', 'nora', 'lily', 'eleanor', 'hannah', 'lillian', 'addison',
        'aubrey', 'ellie', 'stella', 'natalie', 'zoe', 'leah', 'hazel',
        'violet', 'aurora', 'savannah', 'audrey', 'brooklyn', 'bella',
        'claire', 'skylar', 'liam', 'noah', 'william', 'james', 'oliver',
        'benjamin', 'elijah', 'lucas', 'mason', 'logan', 'alexander', 'ethan',
        'jacob', 'michael', 'daniel', 'henry', 'jackson', 'sebastian', 'aiden',
        'matthew', 'samuel', 'david', 'joseph', 'carter', 'owen', 'wyatt',
        'john', 'jack', 'luke', 'jayden', 'dylan', 'grayson', 'levi', 'isaac',
        'gabriel', 'julian', 'mateo', 'anthony', 'jaxon', 'lincoln', 'joshua',
        'christopher', 'andrew', 'theodore', 'caleb', 'ryan', 'asher',
        'nathan', 'thomas', 'leo', 'lucy', 'paisley', 'everly', 'anna',
        'caroline', 'nova', 'genesis', 'emilia', 'kennedy', 'samantha', 'maya',
        'willow', 'kinsley', 'naomi', 'aaliyah', 'elena', 'sarah', 'ariana',
        'allison', 'gabriella', 'alice', 'madelyn', 'cora', 'ruby', 'eva',
        'serenity', 'autumn', 'adeline', 'hailey', 'gianna', 'valentina',
        'isla', 'eliana', 'quinn', 'nevaeh', 'ivy', 'sadie', 'piper', 'lydia',
        'alexa', 'josephine', 'emery', 'julia', 'delilah', 'arianna', 'vivian',
        'kaylee', 'sophie', 'brielle', 'madeline'
    ]
    genders = ['male', 'female']
    account_types = ['savings', 'current']

    # create random accounts for testing purposes
    for persons in range(1, 11):

        # user information initialization
        f_name = choice(names)
        l_name = choice(names)
        age = randint(0, 65)
        gender = choice(genders)
        m_number = randint(9000000000, 9999999999)

        # account information initialization
        account_no = randint(3500000000, 3999999999)
        account_type = choice(account_types)
        date_of_opening = randint(1, 32)

        # instantiation of user and account information
        account = Account(account_no, date_of_opening, account_type, f_name,
                          l_name, age, gender, m_number)

        # creating variables to store in dictionary
        manager.user_info = [
            account.f_name, account.l_name, account.age, account.gender,
            account.m_number, account.account_type, account.date_of_opening,
            account.bank_name, account.ifsc_code
        ]

        # creating a separate list to document total number of users
        name = account.get_user_name()
        manager.existing_users.append(name)

        # saving user information in dictionary
        manager.user_data[account.account_no] = manager.user_info

    # remove file if exists for now
    if path.exists('database.txt'):
        remove('database.txt')
        print('I am here')

    # saving user data on to a file
    with open('database.txt', 'w') as file_handle:
        for key, values in manager.user_data.items():
            file_handle.write(f'{key}, ')
            for items in values:
                file_handle.write(f'{items}, ')
            file_handle.write('\n')
