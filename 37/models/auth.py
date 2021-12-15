import faker


class AuthUserData:
    def __init__(self, username=None, password=None, email=None, firstname=None, surname=None):
        self.username = username
        self.password = password
        self.email = email
        self.firstname = firstname
        self.surname = surname

    @staticmethod
    def random_new_user():
        fake = faker.Faker()
        return AuthUserData(
            username=fake.email(),
            password=fake.password(),
            email=fake.email(),
            firstname=fake.name(),
            surname=fake.name()
        )
