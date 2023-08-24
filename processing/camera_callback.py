from aiogram import types

from processing import messages, storage


async def camera_callback_processing(call: types.CallbackQuery) -> None:
    """
    Handles the callback with information about the selected camera.

    :param call: Callback
    :type call: aiogram.types.CallbackQuery
    :return: None
    """

    storage.hset(f'user-{call.from_user.id}-session', mapping={'camera': call.data})

    lang_code = call.from_user.language_code
    ms = messages(lang_code)
    text = await ms.get_input_sol()

    await call.message.edit_text(text=text)
