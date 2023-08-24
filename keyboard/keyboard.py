from typing import List

import redis
from aiogram import types

from log_config import lg
from utils import Utils

storage = redis.Redis(host='localhost', port=6379, decode_responses=True, db=0)


class InlineKeyboard:
    """Class representing objects of inline buttons."""

    @lg.catch
    def __init__(self):
        """Initializes basic settings."""

        self._utils = Utils()
        self.markup = types.InlineKeyboardMarkup(row_width=2)
        self._curiosity_sols = storage.hget('curiosity', 'last_sol')
        self._opportunity_sols = storage.hget('opportunity', 'last_sol')
        self._spirit_sols = storage.hget('spirit', 'last_sol')
        self.sols_msg_ru = 'солы'
        self.sols_msg_en = 'sols'

        self.cur_btn = types.InlineKeyboardButton(text=f'', callback_data='rover_curiosity')
        self.opp_btn = types.InlineKeyboardButton(text=f'', callback_data='rover_opportunity')
        self.sp_btn = types.InlineKeyboardButton(text=f'', callback_data='rover_spirit')

    @lg.catch
    async def start_buttons(self, lang_code: str) -> types.InlineKeyboardMarkup:
        """
        ВReturns the objects of start menu buttons for selecting a rover.

        :return: Keyboard object
        """

        if lang_code == 'ru':
            c_sols = self.sols_msg_ru
            o_sols = self.sols_msg_ru
            s_sols = self.sols_msg_ru
        else:
            c_sols = self.sols_msg_en
            o_sols = self.sols_msg_en
            s_sols = self.sols_msg_en

        c_text = f'Curiosity ({c_sols}: {self._curiosity_sols})'
        o_text = f'Opportunity ({o_sols}: {self._opportunity_sols})'
        s_text = f'Spirit ({s_sols} {self._spirit_sols})'

        self.cur_btn.text = c_text
        self.opp_btn.text = o_text
        self.sp_btn.text = s_text

        return self.markup.add(self.cur_btn, self.opp_btn, self.sp_btn)

    @staticmethod
    @lg.catch
    async def rovers_cameras(cameras: List) -> types.InlineKeyboardMarkup:
        """
        Forms a keyboard from the list of rover cameras.

        :param cameras: List of cameras of the selected rover
        :type cameras: List
        :return: Keyboard object
        """

        btns = []
        markup = types.InlineKeyboardMarkup(row_width=3)

        for cam in cameras:
            btns.append(types.InlineKeyboardButton(text=cam, callback_data='cam_' + cam))

        return markup.add(*btns)

    @lg.catch
    async def update_curiosity_sol(self) -> None:
        """
        Updates the latest sol of Curiosity.

        :return: None
        """

        sol = await self._utils.get_curiosity_last_sol()
        storage.hset('curiosity', mapping={'last_sol': sol})


if __name__ == '__main__':
    kb = InlineKeyboard()
