from random import choice, randint
import unittest

from bot.config import (NUMBER_USERS, MAX_POSTS_PER_USER, CREATE_USER_URL,
                    CREATE_POST_URL, ADD_RATE_URL, GET_TOKEN_URL)
from bot import user
from bot import post

import requests

class TestGenerateUser(unittest.TestCase):

    def test_all_bot(self):
        post_number = randint(1, MAX_POSTS_PER_USER)
        user_number = NUMBER_USERS

        generator = user.GenerateUser()
        users = generator.generate_users(user_number)
        self.assertEqual(len(users), user_number)

        register = user.RegistrationUser(CREATE_USER_URL)
        tokens = register.register_users(list_of_users=users,
                                         token_url=GET_TOKEN_URL)
        self.assertEqual(len(tokens), user_number)

        post_creater = post.PostCreater(CREATE_POST_URL,
                                        post_number)
        post_ids = post_creater.create_post(tokens)
        self.assertEqual(len(post_ids), user_number*post_number)

        post.LikeCreater(ADD_RATE_URL,
                         tokens, post_ids)
        id = choice(post_ids)
        post_ = requests.get(CREATE_POST_URL+str(id)).json()
        self.assertEqual(post_.get("like_rating")+post_.get("dislike_rating"), NUMBER_USERS)
