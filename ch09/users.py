class Users:
    def __init__(self, first_name, last_name):
        """Initialize variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = '999-999-9999'
        self.user_name = (self.first_name[0]+self.last_name)
        self.email = (first_name+last_name+'@work.com')

    def get_user_info(self):
        print(f'User info for {self.first_name}.')
        print(f'{self.email}, {self.phone_number}')

    def greet_user(self):
        print(f'Good morning {self.first_name}')


# user = Users('Bob', 'Dole')
# print(user.user_name)


# admin_account = Admin('Bob', 'Dole')
# admin_account.show_privileges()
