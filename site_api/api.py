import json
import os
from typing import Dict

import requests


class APIHandler:
    """Class representing the API request handler."""

    def __init__(self, **kwargs):
        """Initializes the initial parameters."""

        self._api_key = os.getenv('KEY')
        self._rover_data = {}

        if kwargs:
            # Формирует словарь с параметрами, необходимыми для запроса фотографий роверов
            self._rover_data = {'rover': kwargs['rover'],
                                'sol': kwargs['sol'],
                                'camera': kwargs['camera']}

    def _gen_url(self, url: str) -> str:
        """
        Generates a correct URL form.

        :param url: URL from config.env
        :type url: str
        :return: URL ready for the request
        """

        return url.format(**self._rover_data, api_key=self._api_key)

    def make_request(self, url: str) -> Dict:
        """
        Performs a request to the specified URL.

        :param url: URL from config.env
        :type url: str
        :return: Request result in JSON format
        """

        response = requests.get(self._gen_url(url))
        response = json.loads(response.text)

        return response


if __name__ == '__main__':
    pass
