import logging
from pyrogram import Client
from vars import var
from pathlib import path
if Path("friday.mp3").is_file():
      os.remove("friday.mp3")

logging.basicConfig(level=logging.INFO)

AnonyBot = Client('Anonymous-Sender',
                  api_id=var.API_ID,
                  api_hash=var.API_HASH,
                  bot_token=var.BOT_TOKEN,
                  plugins=dict(root="plugins"))

AnonyBot.run()
