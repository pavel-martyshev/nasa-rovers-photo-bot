import re
from typing import Callable

from aiogram import types

from log_config import lg

pattern = r'^[^_]*_'


@lg.catch
def replace_call_data(func: Callable):
    async def decorator(call: types.CallbackQuery):
        """
        Removes the beginning of the string up to the underscore symbol.

        :param call: Callback
        :type call: aiogram.types.CallbackQuery
        """

        new_data = re.sub(pattern, '', call.data)
        call.data = new_data
        result = await func(call)
        return result
    return decorator


if __name__ == '__main__':
    pass
