from log_config import lg
from messages import texts


class Messages:
    """Class representing messages"""

    def __init__(self, lang_code: str):
        """Initializes the user's language code."""

        self.lang_code = lang_code

    @lg.catch
    async def get_start_message(self):
        """Returns the start message."""

        if self.lang_code == 'ru':
            return texts.RU_START_MESSAGE
        return texts.EN_START_MESSAGE

    @lg.catch
    async def get_additional_info(self):
        """Returns a message with additional information."""

        if self.lang_code == 'ru':
            return texts.RU_INFO
        return texts.EN_INFO

    @lg.catch
    async def get_input_sol(self):
        """Returns a message about entering the sol."""

        if self.lang_code == 'ru':
            return texts.RU_SOL
        return texts.EN_SOL

    @lg.catch
    async def get_choose_camera(self):
        """Returns a message about selecting a camera."""

        if self.lang_code == 'ru':
            return texts.RU_CAMERA
        return texts.EN_CAMERA

    @lg.catch
    async def get_choose_rover(self):
        """Returns a message about selecting a rover."""

        if self.lang_code == 'ru':
            return texts.RU_ROVER
        return texts.EN_ROVER

    @lg.catch
    async def get_not_photo(self):
        """Returns a message about the absence of photos."""

        if self.lang_code == 'ru':
            return texts.RU_NOT_PHOTO
        return texts.EN_NOT_PHOTO
