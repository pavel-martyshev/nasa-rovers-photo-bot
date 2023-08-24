from aiogram import types
from aiogram import Dispatcher, executor

from utils import Utils
from log_config import lg
from decorators import replace_call_data
from processing import bot, start, rover_callback, camera_callback, sol_message

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
@lg.catch
async def start_message_handler(message: types.Message) -> None:
    """
    Gets the user's start message.

    :param message: Message sent by the user
    :type message: aiogram.types.message
    :return: None
    """

    await start.start_message_processing(message)


@dp.callback_query_handler(lambda call: call.data.startswith('rover_'))
@replace_call_data
@lg.catch
async def rover_callback_handler(call: types.CallbackQuery) -> None:
    """
    Gets the callback with information about the selected rover.

    :param call: Callback
    :type call: aiogram.types.CallbackQuery
    :return: None
    """

    await rover_callback.rover_callback_processing(call)


@dp.callback_query_handler(lambda call: call.data.startswith('cam_'))
@replace_call_data
@lg.catch
async def camera_callback_handler(call: types.CallbackQuery) -> None:
    """
    Gets the callback with information about the selected camera.

    :param call: Callback
    :type call: aiogram.types.CallbackQuery
    :return: None
    """

    await camera_callback.camera_callback_processing(call)


@dp.message_handler(lambda message: message.text.isdigit())
@lg.catch
async def sol_message_handler(message: types.Message) -> None:
    """
    Gets the message with the sol.

    :param message: Message sent by the user
    :type message: aiogram.types.message
    :return: None
    """

    await sol_massage.sol_message_processing(message)


if __name__ == '__main__':
    ut = Utils()
    ut.add_start_info_in_storage()
    executor.start_polling(dp, skip_updates=True)
