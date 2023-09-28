from users import Users


class Privileges:
    def __init__(self):
        self.privileges = ['Add', 'Update', 'Delete']


class Admin(Users):
    """Class for admin user accounts"""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.user_privileges = Privileges()

    def show_privileges(self):
        print(f'{self.user_name} has access to:')
        for privilege in self.user_privileges.privileges:
            print(f' {privilege}')
