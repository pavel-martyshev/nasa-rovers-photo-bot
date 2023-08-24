from aiogram import types

from log_config import lg
from processing import messages, keyboard, storage


@lg.catch
async def rover_callback_processing(call: types.CallbackQuery) -> None:
    """
    Handles the callback with information about the selected rover.

    :param call: Callback
    :type call: aiogram.types.CallbackQuery
    :return: None
    """

    storage.hset(f'user-{call.from_user.id}-session', mapping={'rover': call.data})
    cameras = storage.hget(call.data, 'cameras').split()
    lang_code = call.from_user.language_code
    ms = messages(lang_code)
    kb = keyboard()
    text = await ms.get_choose_camera()

    await call.message.edit_text(text=text, reply_markup=await kb.rovers_cameras(cameras))
