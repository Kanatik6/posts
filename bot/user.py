from faker import Faker

from utils import request


class GenerateUser:

    def generate_users(self, number_of_users: int):
        self.faker = Faker()
        self.names = list()

        usernames = [self.faker.unique.first_name()
                     for x in range(1, number_of_users)]
        passwords = [self.faker.unique.msisdn()
                     for x in range(1, number_of_users)]
        self.users = list(zip(usernames, passwords))


class RegistrationUser:

    def __init__(self, url):
        self.url = url
        self.tokens = list()

    def register_users(self, list_of_users, token_url):
        tokens = list()

        for i in list_of_users:
            request.request(
                self.url,
                data={'username': i[0], 'password': i[1]},
                method='POST')

            request_tokens = request.request(token_url,
                                             data={
                                                 'username': i[0], 'password': i[1]},
                                             method='POST')
            tokens.append(request_tokens)

        success_tokens = [i.get('access') for i in tokens if i]
        return success_tokens
