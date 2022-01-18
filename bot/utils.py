import requests
# стоит ли делать проверки, ифы если ты точно знаешь что это твоя прога и ты не допустишь в ней ошибку?
# потому что если неправильно ввести данные, то прога отвалится. все по pep8


class Request:

    def request(self, url, data=None, method=None, headers=None):
        if method == "POST":
            # print(data, method, headers)
            response = requests.post(url=url,
                                     data=data,
                                     headers=headers)
        elif method == 'GET':
            response = requests.get(url=url)
        else:
            raise TypeError(f'you passed the wrong method, - {method}',)
        return response.json()


request = Request()
