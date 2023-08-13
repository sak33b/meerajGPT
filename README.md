<h1 align="center">
    <span>meerajGPT</span>
  <img width="auto" height="50px" src="asset/p.png"/>
</h1>

## What is meerajGPT?

<p align="center"><i> 
meerajGPT is a Discord bot to give everyone access to a QnA based large language model. 
</i></p>

meerajGPT  is written in Python that uses the [OpenAI API](https://platform.openai.com/docs/api-reference) to have QnA in a predefined discord channel with the `gpt-3.5-turbo` model.

This bot uses the [OpenAI Python Library](https://github.com/openai/openai-python) and [discord.py](https://discordpy.readthedocs.io/).


## Setup


1. Go to https://platform.openai.com/account/api-keys, create a new API key, and fill in `OPENAI_KEY` variable in [responses.py](https://github.com/sak33b/meerajGPT/blob/main/responses.py) or set is as environment variable.
1. Create your own Discord application at https://discord.com/developers/applications
1. Go to the Bot tab and click "Add Bot"
    - Click "Reset Token" and fill in `TOKEN` in [bot.py](https://github.com/sak33b/meerajGPT/blob/main/bot.py)
    - Disable "Public Bot" unless you want your bot to be visible to everyone
    - Enable "Message Content Intent" under "Privileged Gateway Intents"
1. Copy the  server name you want to allow your bot to be used in into `CHAT_CHANNEL`
1. Install dependencies and run the bot
    ```
    pip install -r requirements.txt
    python main.py
    ```
    Note: make sure you are using Python 3.9+ (check with python --version)

## FAQ

> Why isn't my bot responding to commands?

Ensure that the channels your bots have access to allow the bot to have these permissions.
- Send Messages
- Send Messages in Threads
- Create Public Threads
- Manage Threads
- Read Message History
- Use Application Commands
