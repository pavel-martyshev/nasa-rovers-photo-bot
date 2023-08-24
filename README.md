# Telegram-bot [NASA Rovers Photo](https://t.me/nasa_rovers_photo_bot)

This Telegram bot allows you to receive photos from the Curiosity, Opportunity, and Spirit rovers using the NASA API.
The bot provides with the option to choose a rover, rover camera, and sol, and then sends the requested photos.

## Installation and Setup

1. Install the necessary dependencies by running the following command:
    ```bash
    pip install -r requirements.txt
2. Create a bot on Telegram and obtain the token. [Instructions](https://core.telegram.org/bots#botfather)
3. Create a `config.env` file and save variables in it as shown in the example:
    ```
   TOKEN = bot token

   KEY = API key
   PHOTO_ROVERS_URL = https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?sol={sol}&camera={camera}&api_key={api_key}
   CURIOSITY_INFO = https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/?api_key={api_key}

4. Run the bot:
    ```bash
    python bot.py

## Usage

1. Start the bot on Telegram, find it by name, and initiate a conversation.
2. The bot will prompt you to choose a rover (Curiosity, Opportunity, or Spirit) using buttons.
3. After selecting a rover, the bot will prompt you to choose a rover camera using buttons.
4. After selecting a camera, the bot will ask you to enter a sol.
5. Once you enter a sol, the bot will send you photos of the requested rover, camera, and sol (up to 10 images).

## Notes

1. This bot uses the NASA API to retrieve photos from rovers. Ensure that your server has access to the internet.
2. This bot is provided "as is" without warranties or support. You can modify and extend its functionality as you see
   fit.
3. Please ensure that you adhere to the terms of use for the NASA API and Telegram.

## License

This project is distributed under the [MIT License](LICENSE).