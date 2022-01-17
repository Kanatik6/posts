from random import choice

from utils import request


class PostCreater:

    def __init__(self, url, number_of_posts):
        self.url = url
        self.number_of_posts = number_of_posts

    def create_post(self, tokens_list):
        post_ids = list()
        for token in tokens_list:
            response = [request.request(self.url,
                                        data={'title': 'qer'},
                                        headers={
                                            'Authorization': 'Bearer '+token},
                                        method='POST') for i in range(self.number_of_posts)]
            data = response
            [post_ids.append(data_.get('id')) for data_ in data]

        return post_ids


class LikeCreater:

    def __init__(self, url, tokens, post_ids):
        self.url = url
        self.tokens = tokens
        self.post_ids = post_ids
        self._set_like_urls()
        self.create_like()

    def create_like(self):
        for user_token in self.tokens:
            [request.request(
                choice([i, i.replace('like', 'dislike')]),
                headers={'Authorization': 'Bearer '+user_token},
                method='POST') for i in self.like_urls]

    def _set_like_urls(self):
        self.like_urls = [self.url.replace(
            '/1/', f'/{i}/') for i in self.post_ids]
