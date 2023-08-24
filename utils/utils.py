import os

import redis

from site_api import APIHandler
from log_config import lg

storage = redis.Redis(host='yor host', port=6379, decode_responses=True, db='your db')


class Utils:
    """Class representing additional utilities."""

    def __init__(self):
        """Initializes the API request handler."""

        self.api = APIHandler()

    async def get_curiosity_last_sol(self) -> str:
        """
        Returns the latest sol of Curiosity.

        :return: Sol
        """

        url = os.getenv('CURIOSITY_INFO')
        response = self.api.make_request(url)

        return response['rover']['max_sol']

    @staticmethod
    @lg.catch
    def add_start_info_in_storage() -> None:
        """
        Adds the required start information to the storage.

        :return: None
        """

        if 'curiosity' not in storage.keys():
            storage.hset(
                'curiosity', mapping={
                    'last_sol': 0,
                    'cameras': 'FHAZ RHAZ MAST CHEMCAM MAHLI MARDI NAVCAM'
                })
            storage.hset(
                'opportunity', mapping={
                    'last_sol': 5111,
                    'cameras': 'FHAZ RHAZ NAVCAM PANCAM MINITES'
                })
            storage.hset(
                'spirit', mapping={
                    'last_sol': 2208,
                    'cameras': 'FHAZ RHAZ NAVCAM PANCAM MINITES'
                })

            storage.set('chats', '')


if __name__ == '__main__':
    pass
