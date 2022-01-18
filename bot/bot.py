from random import randint

from config import (NUMBER_USERS, MAX_POSTS_PER_USER, CREATE_USER_URL,
                    CREATE_POST_URL, ADD_RATE_URL, GET_TOKEN_URL)
import user
import post


def main():

    post_number = randint(1, MAX_POSTS_PER_USER)
    user_number = NUMBER_USERS

    generator = user.GenerateUser()
    users = generator.generate_users(user_number)

    register = user.RegistrationUser(CREATE_USER_URL)
    tokens = register.register_users(list_of_users=users,
                                     token_url=GET_TOKEN_URL)

    post_creater = post.PostCreater(CREATE_POST_URL,
                                    post_number)
    post_ids = post_creater.create_post(tokens)

    post.LikeCreater(ADD_RATE_URL,
                     tokens, post_ids)
    


if __name__ == '__main__':
    main()
