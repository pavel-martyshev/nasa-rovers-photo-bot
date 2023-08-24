import os

from aiogram import types

from site_api import APIHandler
from processing import bot, storage, messages, keyboard


async def sol_message_processing(message: types.Message) -> None:
    """
    Handles the message with the sol.

    :param message: Message sent by the user
    :type message: aiogram.types.message
    :return: None
    """

    media = []

    rover, camera = storage.hmget(f'user-{message.from_user.id}-session', 'rover', 'camera')
    sol = message.text

    url = os.getenv('PHOTO_ROVERS_URL')
    api = APIHandler(rover=rover, sol=sol, camera=camera)

    lang_code = message.from_user.language_code
    ms = messages(lang_code)
    not_photo_text = await ms.get_not_photo()
    choose_rover_text = await ms.get_choose_rover()

    kb = keyboard()

    result = api.make_request(url)['photos']
    res_len = len(result)

    if result:
        if res_len == 1:
            media = result[0]['img_src']
            await bot.send_photo(chat_id=message.from_user.id, photo=media)
        elif res_len >= 2:
            for elem in result[:10]:
                media.append(types.InputMediaPhoto(elem['img_src']))
            await bot.send_media_group(chat_id=message.from_user.id, media=media)
    else:
        await message.answer(text=not_photo_text)

    await kb.update_curiosity_sol()
    await message.answer(text=choose_rover_text, reply_markup=await kb.start_buttons(lang_code))
