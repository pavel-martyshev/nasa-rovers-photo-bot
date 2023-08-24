from aiogram import types

from processing import bot, keyboard, messages, storage


async def start_message_processing(message: types.Message) -> None:
    """
    Handles the user's start message during the first launch.

    :param message: Message sent by the user
    :type message: aiogram.types.message
    :return: None
    """

    if str(message.from_user.id) not in storage.get('chats').split():
        storage.append('chats', str(message.from_user.id) + ' ')

    lang_code = message.from_user.language_code
    ms = messages(lang_code)
    start_text = await ms.get_start_message()
    info_text = await ms.get_additional_info()
    choose_rover_text = await ms.get_choose_rover()

    kb = keyboard()
    markup = await kb.start_buttons(lang_code)

    await message.answer(text=start_text)
    info_message = await message.answer(text=info_text)

    storage.hset(f'user-{message.from_user.id}-session', mapping={
        'rover': '',
        'camera': '',
        'pin_msg': info_message.message_id
    })

    await kb.update_curiosity_sol()
    await bot.pin_chat_message(chat_id=message.chat.id, message_id=info_message.message_id)
    await message.answer(text=choose_rover_text, reply_markup=markup)
